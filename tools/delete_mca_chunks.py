#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


SECTOR_BYTES = 4096
HEADER_BYTES = SECTOR_BYTES * 2
ENTRIES = 1024


def floor_div(a: int, b: int) -> int:
    return a // b


def local_coord(chunk: int) -> int:
    return chunk % 32


def entry_index(chunk_x: int, chunk_z: int) -> int:
    return local_coord(chunk_x) + local_coord(chunk_z) * 32


def region_name(chunk_x: int, chunk_z: int) -> str:
    return f"r.{floor_div(chunk_x, 32)}.{floor_div(chunk_z, 32)}.mca"


def clear_chunk_entry(path: Path, index: int) -> bool:
    with path.open("r+b") as f:
        header = f.read(HEADER_BYTES)
        if len(header) < HEADER_BYTES:
            raise ValueError(f"{path} is too small to be an MCA file")

        loc_offset = index * 4
        timestamp_offset = SECTOR_BYTES + index * 4
        old_location = header[loc_offset : loc_offset + 4]
        old_timestamp = header[timestamp_offset : timestamp_offset + 4]
        if old_location == b"\x00\x00\x00\x00" and old_timestamp == b"\x00\x00\x00\x00":
            return False

        f.seek(loc_offset)
        f.write(b"\x00\x00\x00\x00")
        f.seek(timestamp_offset)
        f.write(b"\x00\x00\x00\x00")
        return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Delete selected chunks from Minecraft MCA files by clearing header entries.")
    parser.add_argument("--world", required=True, type=Path)
    parser.add_argument("--min-chunk-x", required=True, type=int)
    parser.add_argument("--max-chunk-x", required=True, type=int)
    parser.add_argument("--min-chunk-z", required=True, type=int)
    parser.add_argument("--max-chunk-z", required=True, type=int)
    parser.add_argument("--report", required=True, type=Path)
    args = parser.parse_args()

    targets = ("region", "entities", "poi")
    report = {
        "world": str(args.world),
        "chunkRange": {
            "x": [args.min_chunk_x, args.max_chunk_x],
            "z": [args.min_chunk_z, args.max_chunk_z],
        },
        "blockRangeApprox": {
            "x": [args.min_chunk_x * 16, args.max_chunk_x * 16 + 15],
            "z": [args.min_chunk_z * 16, args.max_chunk_z * 16 + 15],
        },
        "files": {},
        "missingFiles": [],
        "totalRequestedChunksPerTarget": (args.max_chunk_x - args.min_chunk_x + 1)
        * (args.max_chunk_z - args.min_chunk_z + 1),
        "totalClearedEntries": 0,
    }

    for target in targets:
        target_dir = args.world / target
        report["files"][target] = {}
        for chunk_x in range(args.min_chunk_x, args.max_chunk_x + 1):
            for chunk_z in range(args.min_chunk_z, args.max_chunk_z + 1):
                mca = target_dir / region_name(chunk_x, chunk_z)
                if not mca.exists():
                    key = str(mca)
                    if key not in report["missingFiles"]:
                        report["missingFiles"].append(key)
                    continue

                file_report = report["files"][target].setdefault(
                    str(mca),
                    {"requested": 0, "cleared": 0, "alreadyEmpty": 0},
                )
                file_report["requested"] += 1
                changed = clear_chunk_entry(mca, entry_index(chunk_x, chunk_z))
                if changed:
                    file_report["cleared"] += 1
                    report["totalClearedEntries"] += 1
                else:
                    file_report["alreadyEmpty"] += 1

    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
