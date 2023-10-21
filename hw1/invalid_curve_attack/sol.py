#!/usr/bin/env bash
"sage" "--python" "$0"
"exit" "$?"

from Crypto.Util.number import long_to_bytes
from sage.all_cmdline import *
from pwn import *
import sys

p = 0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff
a = 0xffffffff00000001000000000000000000000000fffffffffffffffffffffffc
b = 0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b
n = 0xffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551

def crt_equation_generator():
    try:
        # Generate curve with order with small prime factor
        print(f"Try.")
        b = randint(1, p)
        E = EllipticCurve(GF(p), [a, b])
        N = E.order()
        valid = [factor for factor in prime_factors(N) if factor <= 2**30]
        if len(valid) == 0:
            return None, None
        prime = valid[-1]
        G = E.gen(0) * int(N / prime)
        node = G.xy()
        # send to server (if connected, do not interrupt)
        r = remote('10.113.184.121', 10034)
        r.recvline()
        r.sendlineafter(b'Gx: ', str(node[0]).encode())
        r.sendlineafter(b'Gy: ', str(node[1]).encode())
        data = r.recvline()
        r.close()
    except KeyboardInterrupt:
        return None, None
    # dlog try
    try:
        Q = eval(data)
        Q = E(Q[0], Q[1])
        num = G.discrete_log(Q)
        return num, prime
    except Exception as e:
        print(e, file=sys.stderr)
        return None, None

nums = []
mods = []

for i in range(10):
    num, prime = crt_equation_generator()
    if num is None:
        continue
    nums.append(num)
    mods.append(prime)

while True:
    num, prime = crt_equation_generator()
    if num is None:
        continue
    nums.append(num)
    mods.append(prime)
    #print(f"nums: {nums}")
    #print(f"mods: {mods}")
    flag = long_to_bytes(CRT_list(nums, mods))
    if not flag.startswith(b"FLAG{"):
        continue
    try:
        print(flag.decode())
        break
    except:
        continue

