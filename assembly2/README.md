# Shellcode Optimization (HTB)

This folder contains my solution for a binary exploitation task from HackTheBox, where the goal was to create working shellcode under **50 bytes**.

## Summary

- **Objective:** Run shellcode in a 50-byte buffer.
- **Method:** Iteratively optimized assembly to shrink size.
- Used `xor reg, reg` instead of `mov reg, 0` and removed redundant instructions.
- Verified functionality after every change.
- **Final shellcode:** 49 bytes, successful flag retrieval.

## Tools

- `script.sh`: To assemble and link after each edit.
- HTB shellcoder: To extract shellcode + (`mmap + ctypes`): To test shellcode execution easily.
