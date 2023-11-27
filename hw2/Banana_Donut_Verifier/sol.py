from pwn import *

r = process(['/usr/bin/cat','./input'])

input = r.recv()

r = process(['/usr/bin/cat','./data'])

data = r.recv()

flag = ''

for i in range(1024):
    flag += chr(input[i] ^ data[i] ^ ord('1'))

print(flag.encode())

"""
r = process('./donut-verifier')

r.recv()

r.send(flag.encode())

r.interactive()
"""