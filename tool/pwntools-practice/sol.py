#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib
from pwn import *

r = remote('edu-ctf.csie.org', 54322)

md5_table = dict()

for i in range(2**24 - 1):
    md5_table[hashlib.md5(f'{i}'.encode()).hexdigest()[0:8]] = i

def solve_pow(r):
    target = r.recvuntil(b" :").decode().split("\"")[1]
    r.sendline(str(md5_table[target]).encode())

solve_pow(r)
r.sendline("3".encode())
for i in range(10):
    solve_pow(r)

r.interactive()
r.close()