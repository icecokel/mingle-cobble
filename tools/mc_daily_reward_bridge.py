#!/usr/bin/env python3
"""Grant one random daily reward when a player joins the Minecraft server."""

from __future__ import annotations

import argparse
import json
import os
import random
import re
import subprocess
import threading
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

try:
    from zoneinfo import ZoneInfo
except ImportError:  # pragma: no cover - Python < 3.9 fallback
    ZoneInfo = None


PLAYER_PATTERN = re.compile(r"^[A-Za-z0-9_]{1,16}$")
JOIN_PATTERNS = [
    re.compile(r"\]: (?P<player>[A-Za-z0-9_]{1,16}) joined the game$"),
]

DAILY_REWARDS = [
    {"label": "추가 보상 없음", "weight": 40, "item": None, "count": 0, "summary": "none"},
    {"label": "슈퍼볼 3개", "weight": 25, "item": "cobblemon:great_ball", "count": 3, "summary": "cobblemon:great_ball 3"},
    {"label": "경험치 사탕 XS 2개", "weight": 15, "item": "cobblemon:exp_candy_xs", "count": 2, "summary": "cobblemon:exp_candy_xs 2"},
    {"label": "경험치 사탕 XS 5개", "weight": 10, "item": "cobblemon:exp_candy_xs", "count": 5, "summary": "cobblemon:exp_candy_xs 5"},
    {"label": "부활초 1개", "weight": 5, "item": "cobblemon:revival_herb", "count": 1, "summary": "cobblemon:revival_herb 1"},
    {"label": "하이퍼볼 1개", "weight": 3, "item": "cobblemon:ultra_ball", "count": 1, "summary": "cobblemon:ultra_ball 1"},
    {"label": "기력의 조각 1개", "weight": 2, "item": "cobblemon:revive", "count": 1, "summary": "cobblemon:revive 1"},
]

DEFAULT_STATE = {"version": 1, "timezone": "Asia/Seoul", "players": {}}


def parse_join(line: str) -> str | None:
    for pattern in JOIN_PATTERNS:
        match = pattern.search(line.strip())
        if match:
            return match.group("player")
    return None


def default_state() -> dict:
    return {"version": 1, "timezone": "Asia/Seoul", "players": {}}


def load_state(path: Path) -> dict:
    if not path.exists():
        return default_state()
    with path.open("r", encoding="utf-8") as handle:
        state = json.load(handle)
    if not isinstance(state, dict):
        return default_state()
    state.setdefault("version", 1)
    state.setdefault("timezone", "Asia/Seoul")
    players = state.setdefault("players", {})
    if not isinstance(players, dict):
        state["players"] = {}
    return state


def save_state(path: Path, state: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = path.with_suffix(path.suffix + ".tmp")
    with tmp_path.open("w", encoding="utf-8") as handle:
        json.dump(state, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")
    tmp_path.replace(path)


def resolve_timezone(name: str):
    if ZoneInfo is not None:
        try:
            return ZoneInfo(name)
        except Exception:
            pass
    if name == "Asia/Seoul":
        return timezone(timedelta(hours=9), name="KST")
    return datetime.now().astimezone().tzinfo


def today_kst(now: datetime | None = None, timezone_name: str = "Asia/Seoul") -> tuple[str, datetime]:
    tzinfo = resolve_timezone(timezone_name)
    current = now or datetime.now(tzinfo)
    if current.tzinfo is None:
        current = current.replace(tzinfo=tzinfo)
    current = current.astimezone(tzinfo)
    return current.date().isoformat(), current


def can_claim(state: dict, player: str, today: str) -> bool:
    players = state.get("players", {})
    if not isinstance(players, dict):
        return True
    record = players.get(player)
    if not isinstance(record, dict):
        return True
    return record.get("last_claim_date") != today


def record_claim(state: dict, player: str, today: str, now: datetime, reward_summary: str) -> None:
    state.setdefault("version", 1)
    state.setdefault("timezone", "Asia/Seoul")
    players = state.setdefault("players", {})
    players[player] = {
        "last_claim_date": today,
        "last_claim_at": now.isoformat(),
        "last_reward": reward_summary,
    }


def choose_reward(rng: random.Random) -> dict:
    weights = [reward["weight"] for reward in DAILY_REWARDS]
    return rng.choices(DAILY_REWARDS, weights=weights, k=1)[0]


def resolve_state_path(server_dir: Path, state_path: Path) -> Path:
    if state_path.is_absolute():
        return state_path
    return server_dir / state_path


def send_command(screen_session: str, command: str, dry_run: bool = False) -> None:
    if dry_run:
        print(command)
        return
    subprocess.run(
        ["screen", "-S", screen_session, "-p", "0", "-X", "stuff", command + "\r"],
        check=True,
    )


def send_daily_message(player: str, message: str, screen_session: str, dry_run: bool = False) -> None:
    payload = [
        {"text": "[Daily] ", "color": "gold"},
        {"text": message, "color": "green"},
    ]
    command = f"tellraw {player} {json.dumps(payload, ensure_ascii=False)}"
    send_command(screen_session, command, dry_run)


def grant_daily_if_available(player: str, args: argparse.Namespace, rng: random.Random) -> str | None:
    if not PLAYER_PATTERN.fullmatch(player):
        raise ValueError(f"invalid Minecraft player name: {player!r}")

    state_path = resolve_state_path(args.server_dir, args.state_path)
    state = load_state(state_path)
    today, now = today_kst(timezone_name=args.timezone)

    if not can_claim(state, player, today):
        print(f"[daily] {player}: already claimed for {today}", flush=True)
        return None

    reward = choose_reward(rng)
    if reward["item"]:
        send_command(args.screen_session, f"give {player} {reward['item']} {reward['count']}", args.dry_run)
    send_daily_message(player, f"오늘 데일리 보상: {reward['label']}", args.screen_session, args.dry_run)

    if not args.dry_run:
        state["timezone"] = args.timezone
        record_claim(state, player, today, now, reward["summary"])
        save_state(state_path, state)

    print(f"[daily] {player}: granted {reward['summary']} for {today}", flush=True)
    return reward["summary"]


def schedule_grant(player: str, args: argparse.Namespace, rng: random.Random) -> None:
    def run_grant() -> None:
        try:
            grant_daily_if_available(player, args, rng)
        except Exception as exc:
            print(f"[daily] failed for {player}: {exc}", flush=True)

    timer = threading.Timer(args.join_delay, run_grant)
    timer.daemon = True
    timer.start()


def follow_log(args: argparse.Namespace) -> None:
    log_path = args.server_dir / "logs/latest.log"
    rng = random.Random()
    with log_path.open("r", encoding="utf-8", errors="replace") as handle:
        if not args.from_start:
            handle.seek(0, os.SEEK_END)
        while True:
            line = handle.readline()
            if not line:
                time.sleep(args.poll_interval)
                continue
            player = parse_join(line)
            if not player:
                continue
            print(f"[daily] join detected: {player}", flush=True)
            schedule_grant(player, args, rng)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Minecraft daily reward bridge")
    parser.add_argument("--server-dir", type=Path, default=Path("/home/icenux/minecraft/mingle-lounge"))
    parser.add_argument("--screen-session", default="mingle-sample")
    parser.add_argument("--state-path", type=Path, default=Path("data/daily-rewards-state.json"))
    parser.add_argument("--timezone", default="Asia/Seoul")
    parser.add_argument("--join-delay", type=float, default=3.0)
    parser.add_argument("--poll-interval", type=float, default=0.25)
    parser.add_argument("--from-start", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--once-player", help="Grant once for this player and exit")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.once_player:
        grant_daily_if_available(args.once_player, args, random.Random())
        return 0
    follow_log(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
