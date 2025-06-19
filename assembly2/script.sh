#!/bin/bash

# Usage: ./build.sh yourfile.asm

if [ -z "$1" ]; then
  echo "Usage: $0 filename.s"
  exit 1
fi

ASMFILE="$1"
BASENAME="${ASMFILE%.s}"
OUTFILE="${BASENAME}"

# Assemble
nasm -f elf64 "$ASMFILE" -o "${BASENAME}.o"
if [ $? -ne 0 ]; then
  echo "Assembly failed"
  exit 1
fi

# Link
ld "${BASENAME}.o" -o "$OUTFILE"
if [ $? -ne 0 ]; then
  echo "Linking failed"
  exit 1
fi

echo "Build successful: ./$OUTFILE"
