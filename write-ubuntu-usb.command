#!/bin/zsh
set -u

LOG=/tmp/ubuntu-usb-write.log
ISO=/tmp/ubuntu-26.04-desktop-amd64.iso
DISK=/dev/disk4
RDISK=/dev/rdisk4

: > "$LOG"
echo "Starting Ubuntu USB write at $(date)" | tee -a "$LOG"
echo "Target: $DISK / $RDISK" | tee -a "$LOG"
echo "ISO: $ISO" | tee -a "$LOG"
echo
echo "This will overwrite the USB drive at $DISK."
echo "Enter your macOS password when sudo asks for it."
echo

diskutil unmountDisk "$DISK" 2>&1 | tee -a "$LOG"
sudo /bin/dd if="$ISO" of="$RDISK" bs=4m 2>&1 | tee -a "$LOG"
DD_STATUS=${pipestatus[1]}
/bin/sync
echo "dd_status=$DD_STATUS" | tee -a "$LOG"

if [ "$DD_STATUS" -eq 0 ]; then
  diskutil eject "$DISK" 2>&1 | tee -a "$LOG"
  echo "Finished successfully at $(date)" | tee -a "$LOG"
else
  echo "Write failed at $(date)" | tee -a "$LOG"
fi

echo
echo "Log: $LOG"
echo "Press Enter to close this window."
read
