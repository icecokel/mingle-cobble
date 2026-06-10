#!/usr/bin/env python3
"""Bridge Minecraft chat questions to Hermes/Codex and answer in-game.

This script is intentionally small and dependency-free. It watches
logs/latest.log for player chat messages, asks Hermes or Codex using read-only
server documentation context, and sends the answer back through the Minecraft
server console. It can also save short player-requested memos.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
import zipfile
from pathlib import Path


CHAT_PATTERNS = [
    re.compile(r"\]: (?:\[Not Secure\] )?<(?P<player>[A-Za-z0-9_]{1,16})> (?P<message>.+)$"),
    re.compile(r"\]: \[CHAT\] <(?P<player>[A-Za-z0-9_]{1,16})> (?P<message>.+)$"),
]


def parse_chat(line: str) -> tuple[str, str] | None:
    for pattern in CHAT_PATTERNS:
        match = pattern.search(line)
        if match:
            return match.group("player"), match.group("message").strip()
    return None


def clean_answer(text: str, max_chars: int) -> str:
    lines = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("session_id:"):
            continue
        if line.startswith("OpenAI Codex "):
            continue
        lines.append(line)
    answer = " ".join(lines).strip()
    if not answer:
        answer = "답변을 생성하지 못했습니다."
    if len(answer) > max_chars:
        answer = answer[: max_chars - 1].rstrip() + "..."
    return answer


def parse_memo_request(message: str) -> str | None:
    text = message.strip()
    patterns = [
        r"^메모\s*[:：]\s*(?P<memo>.+)$",
        r"^메모해줘\s+(?P<memo>.+)$",
        r"^메모해\s+(?P<memo>.+)$",
        r"^기억해줘\s+(?P<memo>.+)$",
        r"^기억해\s+(?P<memo>.+)$",
    ]
    for pattern in patterns:
        match = re.match(pattern, text)
        if match:
            memo = match.group("memo").strip()
            return memo or None
    return None


def append_memo(path: Path, player: str, memo: str, now: str | None = None) -> None:
    if not re.fullmatch(r"[A-Za-z0-9_]{1,16}", player):
        raise ValueError(f"invalid Minecraft player name: {player!r}")
    path.parent.mkdir(parents=True, exist_ok=True)
    record = {
        "at": now or time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "player": player,
        "memo": memo,
    }
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def load_recent_memos(path: Path, limit: int) -> list[str]:
    if limit <= 0 or not path.exists():
        return []
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    recent = []
    for line in lines[-limit:]:
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            continue
        at = str(record.get("at", "")).strip()
        player = str(record.get("player", "")).strip()
        memo = str(record.get("memo", "")).strip()
        if memo:
            recent.append(f"{at} {player}: {memo}".strip())
    return recent


def _clean_metadata_value(value) -> str:
    if value is None:
        return ""
    if isinstance(value, dict):
        value = value.get("en_us") or value.get("en_us".upper()) or next(iter(value.values()), "")
    text = str(value).replace("\n", " ").strip()
    return re.sub(r"\s+", " ", text)


def _shorten(text: str, max_chars: int) -> str:
    if len(text) <= max_chars:
        return text
    return text[: max_chars - 1].rstrip() + "..."


def _parse_mods_toml(text: str) -> dict[str, str]:
    metadata: dict[str, str] = {}
    for source_key, target_key in [
        ("modId", "id"),
        ("displayName", "name"),
        ("version", "version"),
        ("description", "description"),
    ]:
        match = re.search(rf"(?ms)^\s*{source_key}\s*=\s*(?:'''(?P<triple>.*?)'''|\"(?P<double>.*?)\")", text)
        if match:
            metadata[target_key] = _clean_metadata_value(match.group("triple") or match.group("double"))
    return metadata


def _read_mod_metadata(jar_path: Path) -> dict[str, str] | None:
    try:
        with zipfile.ZipFile(jar_path) as jar:
            names = set(jar.namelist())
            for metadata_name in ("fabric.mod.json", "quilt.mod.json"):
                if metadata_name in names:
                    raw = json.loads(jar.read(metadata_name).decode("utf-8", errors="replace"))
                    return {
                        "id": _clean_metadata_value(raw.get("id")),
                        "name": _clean_metadata_value(raw.get("name")),
                        "version": _clean_metadata_value(raw.get("version")),
                        "description": _clean_metadata_value(raw.get("description")),
                    }
            if "META-INF/mods.toml" in names:
                return _parse_mods_toml(jar.read("META-INF/mods.toml").decode("utf-8", errors="replace"))
    except (OSError, zipfile.BadZipFile, json.JSONDecodeError):
        return None
    return None


def load_installed_mod_summaries(mods_dir: Path, limit: int) -> list[str]:
    if limit <= 0 or not mods_dir.exists():
        return []
    summaries = []
    jars = sorted(mods_dir.glob("*.jar"), key=lambda path: path.name.lower())
    for jar_path in jars[:limit]:
        metadata = _read_mod_metadata(jar_path) or {}
        mod_id = metadata.get("id", "")
        name = metadata.get("name", "") or mod_id
        version = metadata.get("version", "")
        description = metadata.get("description", "")
        if not name:
            summaries.append(jar_path.stem)
            continue
        display = name
        if mod_id and mod_id != name:
            display = f"{display} ({mod_id})"
        if version:
            display = f"{display} {version}"
        if description:
            display = f"{display} - {_shorten(description, 160)}"
        summaries.append(display)
    if len(jars) > limit:
        summaries.append(f"... and {len(jars) - limit} more installed mod jar(s).")
    return summaries


def extract_question(message: str, prefix: str) -> str | None:
    text = message.strip()
    if not text:
        return None
    if prefix:
        if not text.startswith(prefix):
            return None
        question = text[len(prefix) :].strip()
        return question or None
    return text


def default_extra_doc_paths(server_dir: Path) -> list[Path]:
    return [
        server_dir / "cobblemon-newbie-guide.md",
        server_dir / "cobblemon-mod-usage-guide.md",
        server_dir / "cobblemon-client-setup-guide.md",
    ]


def build_prompt(
    question: str,
    docs_dir: Path,
    memo_context: str = "",
    mod_context: str = "",
    extra_doc_paths: list[Path] | None = None,
) -> str:
    memo_block = ""
    if memo_context:
        memo_block = f"""\

Recent player-requested memos:
{memo_context}
"""
    mod_block = ""
    if mod_context:
        mod_block = f"""\

Local installed mod metadata:
{mod_context}
"""
    extra_doc_block = ""
    if extra_doc_paths:
        extra_doc_block = "\n".join(str(path) for path in extra_doc_paths)
        extra_doc_block = f"""\

Additional local player guides to inspect when relevant:
{extra_doc_block}
"""
    return f"""\
You answer Minecraft in-game questions for the private icecoke-cobblemon server.

Rules:
- Answer in Korean.
- Use the local server docs under {docs_dir} and the installed mod metadata as the highest-priority source for this server.
- You may use general Minecraft, Fabric, Cobblemon, and installed mod knowledge when the local docs are incomplete.
- When using general knowledge, mention uncertainty if it may differ for Minecraft 1.21.1, Fabric, Cobblemon 1.6.1, or the installed mod version.
- You may also use the recent player-requested memos provided below.
- Treat the docs as read-only. Do not modify files. Do not run server-changing commands.
- Never reveal OAuth tokens, auth files, API keys, secrets, or hidden credentials.
- If the docs do not contain enough information, say what needs to be checked.
- Keep the final answer short enough for Minecraft chat, preferably 1-3 sentences.
{memo_block}
{mod_block}
{extra_doc_block}

Question from Minecraft chat:
{question}
"""


def run_hermes(
    question: str,
    server_dir: Path,
    docs_dir: Path,
    timeout: int,
    max_chars: int,
    memo_context: str = "",
    mod_context: str = "",
    extra_doc_paths: list[Path] | None = None,
) -> str:
    prompt = build_prompt(question, docs_dir, memo_context, mod_context, extra_doc_paths)
    cmd = [
        "/home/icenux/.local/bin/hermes",
        "chat",
        "--quiet",
        "--source",
        "minecraft-bridge",
        "--max-turns",
        "4",
        "--query",
        prompt,
    ]
    result = subprocess.run(
        cmd,
        cwd=server_dir,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=timeout,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(f"hermes exited {result.returncode}: {result.stdout.strip()[:500]}")
    return clean_answer(result.stdout, max_chars)


def run_codex(
    question: str,
    server_dir: Path,
    docs_dir: Path,
    timeout: int,
    max_chars: int,
    memo_context: str = "",
    mod_context: str = "",
    extra_doc_paths: list[Path] | None = None,
) -> str:
    prompt = build_prompt(question, docs_dir, memo_context, mod_context, extra_doc_paths)
    output_path = Path("/tmp/mc-hermes-bridge-codex.out")
    if output_path.exists():
        output_path.unlink()
    cmd = [
        "codex",
        "exec",
        "--sandbox",
        "read-only",
        "--skip-git-repo-check",
        "--cd",
        str(server_dir),
        "--output-last-message",
        str(output_path),
        prompt,
    ]
    result = subprocess.run(
        cmd,
        cwd=server_dir,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=timeout,
        check=False,
    )
    if output_path.exists():
        return clean_answer(output_path.read_text(), max_chars)
    if result.returncode != 0:
        raise RuntimeError(f"codex exited {result.returncode}: {result.stdout.strip()[:500]}")
    return clean_answer(result.stdout, max_chars)


def split_chunks(text: str, size: int) -> list[str]:
    chunks = []
    remaining = text
    while remaining:
        chunks.append(remaining[:size])
        remaining = remaining[size:]
    return chunks


def send_tellraw(player: str, answer: str, screen_session: str, dry_run: bool) -> None:
    if not re.fullmatch(r"[A-Za-z0-9_]{1,16}", player):
        raise ValueError(f"invalid Minecraft player name: {player!r}")
    for chunk in split_chunks(answer, 220):
        payload = [
            {"text": "[Hermes] ", "color": "aqua"},
            {"text": chunk, "color": "white"},
        ]
        command = f"tellraw {player} {json.dumps(payload, ensure_ascii=False)}"
        if dry_run:
            print(command)
            continue
        subprocess.run(
            ["screen", "-S", screen_session, "-p", "0", "-X", "stuff", command + "\r"],
            check=True,
        )


def should_reopen_log(log_path: Path, handle) -> bool:
    try:
        current = log_path.stat()
        opened = os.fstat(handle.fileno())
    except OSError:
        return True
    if (current.st_dev, current.st_ino) != (opened.st_dev, opened.st_ino):
        return True
    return current.st_size < handle.tell()


def open_log(log_path: Path, from_start: bool):
    handle = log_path.open("r", encoding="utf-8", errors="replace")
    if not from_start:
        handle.seek(0, os.SEEK_END)
    return handle


def answer_question(args: argparse.Namespace, player: str, question: str) -> str:
    if len(question) > args.max_question_chars:
        return f"질문이 너무 깁니다. {args.max_question_chars}자 이하로 줄여 주세요."
    memo_path = args.memo_path if args.memo_path.is_absolute() else args.server_dir / args.memo_path
    memo_context = "\n".join(load_recent_memos(memo_path, args.memo_limit))
    mods_dir = args.mods_dir if args.mods_dir.is_absolute() else args.server_dir / args.mods_dir
    mod_context = "\n".join(load_installed_mod_summaries(mods_dir, args.mod_limit))
    extra_doc_paths = default_extra_doc_paths(args.server_dir)
    try:
        if args.engine == "hermes":
            return run_hermes(
                question,
                args.server_dir,
                args.docs_dir,
                args.timeout,
                args.max_answer_chars,
                memo_context,
                mod_context,
                extra_doc_paths,
            )
        if args.engine == "codex":
            return run_codex(
                question,
                args.server_dir,
                args.docs_dir,
                args.timeout,
                args.max_answer_chars,
                memo_context,
                mod_context,
                extra_doc_paths,
            )
        try:
            return run_hermes(
                question,
                args.server_dir,
                args.docs_dir,
                args.timeout,
                args.max_answer_chars,
                memo_context,
                mod_context,
                extra_doc_paths,
            )
        except Exception as hermes_error:
            print(f"[bridge] Hermes failed, falling back to Codex: {hermes_error}", file=sys.stderr)
            return run_codex(
                question,
                args.server_dir,
                args.docs_dir,
                args.timeout,
                args.max_answer_chars,
                memo_context,
                mod_context,
                extra_doc_paths,
            )
    except subprocess.TimeoutExpired:
        return "응답 시간이 초과됐습니다. 잠시 후 다시 질문해 주세요."
    except Exception as exc:
        return f"답변 생성 중 오류가 발생했습니다: {str(exc)[:160]}"


def follow_log(args: argparse.Namespace) -> None:
    log_path = args.server_dir / "logs/latest.log"
    last_answer_at: dict[str, float] = {}
    with open_log(log_path, args.from_start) as handle:
        while True:
            line = handle.readline()
            if not line:
                if should_reopen_log(log_path, handle):
                    print(f"[bridge] reopening log file: {log_path}", flush=True)
                    handle.close()
                    handle = open_log(log_path, False)
                time.sleep(args.poll_interval)
                continue
            parsed = parse_chat(line)
            if not parsed:
                continue
            player, message = parsed
            memo = parse_memo_request(message)
            if memo:
                memo_path = args.memo_path if args.memo_path.is_absolute() else args.server_dir / args.memo_path
                if args.dry_run:
                    print(f"memo {player}: {memo}")
                else:
                    append_memo(memo_path, player, memo)
                send_tellraw(player, "메모해뒀습니다.", args.screen_session, args.dry_run)
                print(f"[bridge] memo from {player}: {memo}", flush=True)
                continue
            question = extract_question(message, args.prefix)
            if not question:
                continue
            now = time.monotonic()
            if now - last_answer_at.get(player, 0) < args.cooldown:
                continue
            last_answer_at[player] = now
            print(f"[bridge] {player}: {question}", flush=True)
            answer = answer_question(args, player, question)
            send_tellraw(player, answer, args.screen_session, args.dry_run)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Minecraft chat to Hermes/Codex bridge")
    parser.add_argument("--server-dir", type=Path, default=Path("/home/icenux/minecraft/mingle-lounge"))
    parser.add_argument("--docs-dir", type=Path, default=Path("/home/icenux/minecraft/mingle-lounge/docs"))
    parser.add_argument("--screen-session", default="mingle-sample")
    parser.add_argument("--prefix", default="", help="Optional chat prefix. Empty means every player chat message is handled.")
    parser.add_argument("--memo-path", type=Path, default=Path("data/hermes-memos.jsonl"))
    parser.add_argument("--memo-limit", type=int, default=12)
    parser.add_argument("--mods-dir", type=Path, default=Path("mods"))
    parser.add_argument("--mod-limit", type=int, default=140)
    parser.add_argument("--engine", choices=["hermes", "codex", "auto"], default="auto")
    parser.add_argument("--timeout", type=int, default=90)
    parser.add_argument("--cooldown", type=float, default=10.0)
    parser.add_argument("--poll-interval", type=float, default=0.25)
    parser.add_argument("--max-question-chars", type=int, default=500)
    parser.add_argument("--max-answer-chars", type=int, default=420)
    parser.add_argument("--from-start", action="store_true")
    parser.add_argument("--dry-run", action="store_true", help="Print tellraw commands instead of sending them")
    parser.add_argument("--once-player", help="Answer one question for this player and exit")
    parser.add_argument("--once-question", help="Answer one question and exit")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.once_question:
        player = args.once_player or "Icecokel"
        answer = answer_question(args, player, args.once_question)
        send_tellraw(player, answer, args.screen_session, args.dry_run)
        if args.dry_run:
            print(answer)
        return 0
    follow_log(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
