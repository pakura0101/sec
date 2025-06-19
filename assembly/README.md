# 🔐 XOR Shellcode Decoder & Executor

This Python script is designed to:
- Extract `movabs rax, ...` and `movabs rbx, ...` instructions from the `.text` section of a given ELF binary.
- Decode the shellcode by XORing each `rax` value with the single `rbx` value.
- Allocate executable memory, write the decoded shellcode into it, and execute it using Python's `ctypes`.

## 📁 File Structure

├── loaded_shellcode # The ELF binary containing encoded shellcode
├── decode_execute.py # This script
└── README.md # You're here!


## ⚙️ Requirements

- Python 3.x
- [pwntools]
- ELF file from HTB task 1

Install dependencies:

pip install pwntools



