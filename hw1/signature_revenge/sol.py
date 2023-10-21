#!/usr/bin/env bash
"cp" "$0" "/tmp/tmp.sage"
"sage" "/tmp/tmp.sage"
"rm" "/tmp/tmp.sage" "/tmp/tmp.sage.py"
"exit" "$?"

from Crypto.Util.number import long_to_bytes, bytes_to_long
from sage.all import *
from hashlib import sha256, md5
from ecdsa import SECP256k1

E = SECP256k1
G, n = E.generator, E.order
P = (70427896289635684269185763735464004880272487387417064603929487585697794861713, 83106938517126976838986116917338443942453391221542116900720022828358221631968)
sig1 = (26150478759659181410183574739595997895638116875172347795980556499925372918857, 50639168022751577246163934860133616960953696675993100806612269138066992704236)
sig2 = (8256687378196792904669428303872036025324883507048772044875872623403155644190, 90323515158120328162524865800363952831516312527470472160064097576156608261906)

h1 = bytes_to_long(sha256(b"https://www.youtube.com/watch?v=IBnrn2pnPG8").digest())
h2 = bytes_to_long(sha256(b"https://www.youtube.com/watch?v=1H2cyhWYXrE").digest())
r1, s1 = sig1
r2, s2 = sig2

# t = -s1^(-1)s2r1r2^(-1)
# u = s1^(-1)r1h2r2^(-1) - s1^(-1)h1

t = -pow(s1, -1, n) * s2 * r1 * pow(r2, -1, n)
u = pow(s1, -1, n)* r1 * h2  * pow(r2, -1, n) - pow(s1, -1, n) * h1

# k1 + tk2 + u = 0 mod n
# k1 = m1 * 2^128 + m2
# k2 = m2 * 2^128 + m1
# m1 * 2^128 + m2 + (m2 * 2^128 + m1)t + u = 0 mod n
# m1 * (2^128 + t) + m2 * (1 + t * 2^128) + u = 0 mod n
# m1 * (2^128 + t) + m2 * (1 + t * 2^128) = -u mod n
# m1 * (2^128 + t) = -u - m2 * (1 + t * 2^128) mod n
# m1 = (-u - m2 * (1 + t * 2^128)) * (2^128 + t)^(-1) mod n
# m1 + m2 * (1 + t * 2^128) * (2^128 + t)^(-1) = -u * (2^128 + t)^(-1) mod n
# m1 + m2 * (1 + t * 2^128) * (2^128 + t)^(-1) + u * (2^128 + t)^(-1) = 0 mod n

t1 = (1 + t * pow(2, 128)) * pow(pow(2, 128) + t, -1, n)
u1 = u * pow(pow(2, 128) + t, -1, n)

# m1 + m2 * t1 + u1 = 0 mod n
n, t1, u1, K = int(n), int(t1), int(u1), pow(2, 128)
M = [
        [3 * n, 0, 0],
        [t1, 1, 0],
        [u1, 0, K],
    ]
L = matrix(M).LLL()


target = None
v = []
for i in range(3):
    if L[i][2] == K:
        target = L[i]
    elif L[i][2] == 0:
        v.append(L[i])

if target:
    M1 = -target[0]
    M2 = target[1]
else:
    print(L)
    print("LLL Not Found")
    exit(1)

m1 = long_to_bytes(M1)
m2 = long_to_bytes(M2)
k1 = bytes_to_long(m1 + m2)
k2 = bytes_to_long(m2 + m1)

# s1 = k1^(-1)(h1 + d * r1) mod n
# s1 * k1 = h1 + d * r1 mod n
# s1 * k1 - h1 = d * r1 mod n
# s1 * k1 * r1^(-1) - h1 * r1^(-1) = d mod n

d = int(s1 * k1 * pow(r1, -1, n) - h1 * pow(r1, -1, n))
assert d == int(s2 * k2 * pow(r2, -1, n) - h2 * pow(r2, -1, n))

if m1 == md5(d.to_bytes(32, "big")).digest() and m2 == md5(d.to_bytes(32, "big")[::-1]).digest():
    flag = b'FLAG{' + long_to_bytes(d).split(b'FLAG{')[1]
    print(flag.decode())
    exit()

print(L)

# vt + c * v[i]
coefficient = 5
for i in range(len(v)):
    for j in range(1, coefficient):
        m1 = long_to_bytes((M1 + -v[i][0] * j) % n)
        m2 = long_to_bytes((M2 + v[i][1] * j) % n)
        k1 = bytes_to_long(m1 + m2)
        k2 = bytes_to_long(m2 + m1)

        d = int(s1 * k1 * pow(r1, -1, n) - h1 * pow(r1, -1, n))
        
        if m1 == md5(d.to_bytes(32, "big")).digest() and m2 == md5(d.to_bytes(32, "big")[::-1]).digest():
            flag = b'FLAG{' + long_to_bytes(d).split(b'FLAG{')[1]
            print(flag.decode())
            exit()
