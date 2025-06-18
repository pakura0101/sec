from pwn import *
import mmap
import ctypes


e = ELF("loaded_shellcode")
entry = e.entrypoint
text= e.get_section_by_name(".text").header
code = e.read(text['sh_addr'],text['sh_size'])
context.arch = e.arch
discode = disasm(code, text['sh_addr'])
rax_values = re.findall(r"movabs\s+rax,\s+0x([0-9a-fA-F]+)", discode)
rbx_value = re.findall(r"movabs\s+rbx,\s+0x([0-9a-fA-F]+)", discode)

result = b''

rbx_int = int(rbx_value[0], 16)
for rax_hex in reversed(rax_values):
    rax_int = int(rax_hex, 16)
    xored = rax_int ^ rbx_int
    xor_bytes = xored.to_bytes(8, byteorder = 'big')
    result += xor_bytes

mem = mmap.mmap(-1, len(result), prot=mmap.PROT_READ | mmap.PROT_WRITE | mmap.PROT_EXEC)
mem.write(result)
mem.seek(0)
shell_func = ctypes.CFUNCTYPE(None)(ctypes.addressof(ctypes.c_char.from_buffer(mem)))

shell_func()
