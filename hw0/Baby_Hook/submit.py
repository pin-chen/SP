#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
import hashlib
import sys

from pwn import *

if len(sys.argv) < 2:
    print("usage: {} solver-program".format(sys.argv[0]))
    sys.exit(-1);

r = remote('edu-ctf.zoolab.org', 10002)

def upload(fn):
    r.recvuntil(b'Give me your share object:\n')
    with open(fn, 'rb') as f: z = f.read()
    print("\x1b[1;32m** local md5({}): {}\x1b[m".format(fn, hashlib.md5(z).hexdigest()))
    z = base64.b64encode(z)
    r.sendline(z)

upload(sys.argv[1])
flag = r.recvuntil(b'}')
r.close()
print(flag.decode())