#!/usr/bin/env python
from pwn import *
from Crypto.Cipher import AES

def padding_oracle_attack(r, ct, iv):
    block_len = 16
    pt = b""
    for i in range(block_len - 1, -1, -1):
        for c in range(128, 256):
            iv[i] ^= c
            r.sendline((iv + ct).hex().encode())
            ret = r.recvline()
            if ret == b'Well received :)\n':
                pt = bytes([c ^ 0x80]) + pt
                iv[i] ^= 0x80
                break
            else:
                iv[i] ^= c
        else:
            pt = bytes([0x80]) + pt
            iv[i] ^= 0x80
    return pt

r = remote('edu-ctf.zoolab.org', 10004)
output = bytes.fromhex(r.recvline(keepends=False).decode())

iv = output[:16]
ct = output[16:]
pt = b""

N = len(ct) // 16

for i in range(N):
    pt += padding_oracle_attack(r, ct[i * 16 : (i + 1) * 16], bytearray(iv))
    iv = ct[i * 16 : (i + 1) * 16]

print(pt.split(b'}')[0].decode() + "}")

r.close()
