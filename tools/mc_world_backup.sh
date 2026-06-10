#!/usr/bin/env bash
set -euo pipefail

SERVER_DIR="${SERVER_DIR:-/home/icenux/minecraft/icecoke-cobblemon-173-test}"
SESSION="${SESSION:-icecoke-173}"
BACKUP_DIR="${BACKUP_DIR:-backups}"
LOCK_FILE="${LOCK_FILE:-/tmp/icecoke-cobblemon-173-world-backup.lock}"
SAVE_WAIT_SECONDS="${SAVE_WAIT_SECONDS:-10}"

cd "$SERVER_DIR"
mkdir -p "$BACKUP_DIR" logs

exec 9>"$LOCK_FILE"
if ! flock -n 9; then
  echo "[$(date -Is)] backup already running; skip"
  exit 0
fi

if [ ! -d world ]; then
  echo "[$(date -Is)] missing world directory: $SERVER_DIR/world" >&2
  exit 1
fi

save_disabled=0
reenable_saves() {
  if [ "$save_disabled" -eq 1 ]; then
    echo "[$(date -Is)] sending save-on to ${SESSION}"
    screen -S "$SESSION" -p 0 -X stuff $'save-on\r' || true
  fi
}
trap reenable_saves EXIT

if screen -list | grep -q "[.]${SESSION}[[:space:]]"; then
  echo "[$(date -Is)] sending save-off to ${SESSION}"
  screen -S "$SESSION" -p 0 -X stuff $'save-off\r'
  save_disabled=1
  echo "[$(date -Is)] sending save-all flush to ${SESSION}"
  screen -S "$SESSION" -p 0 -X stuff $'save-all flush\r'
  sleep "$SAVE_WAIT_SECONDS"
else
  echo "[$(date -Is)] screen session not running: ${SESSION}; backing up current disk state"
fi

timestamp="$(date +%Y%m%d-%H%M%S)"
backup="${BACKUP_DIR}/world-auto-backup-${timestamp}.tar.gz"
tmp="${backup}.tmp"

echo "[$(date -Is)] creating ${backup}"
tar -czf "$tmp" world
mv "$tmp" "$backup"

reenable_saves
save_disabled=0

sha256sum "$backup" > "${backup}.sha256"
sha256sum -c "${backup}.sha256"
ls -lh "$backup" "${backup}.sha256"
echo "[$(date -Is)] backup complete: ${backup}"
