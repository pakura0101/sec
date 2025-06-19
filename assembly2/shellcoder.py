#!/usr/bin/python3

import sys
from pwn import *
import mmap
import ctypes

context(os="linux", arch="amd64", log_level="error")

file = ELF(sys.argv[1])
shellcode = file.section(".text")
print(len(file.get_section_by_name(".text").data()))
shell_hex= shellcode.hex()

print(shell_hex)

mem = mmap.mmap(-1, len(shellcode), prot=mmap.PROT_READ | mmap.PROT_WRITE | mmap.PROT_EXEC)
mem.write(shellcode)
mem.seek(0)
shell_func = ctypes.CFUNCTYPE(None)(ctypes.addressof(ctypes.c_char.from_buffer(mem)))

shell_func()