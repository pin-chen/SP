#!/usr/bin/env bash
"sage" "--python" "$0"
"exit" "$?"

#from secret import FLAG
FLAG = b'FLAG{...}'
from Crypto.Util.number import bytes_to_long
from os import urandom
from sage.all import *
class LFSR:
    def __init__(self, tap, state):
        self._tap = tap
        self._state = state

    def getbit(self):
        f = sum([self._state[i] for i in self._tap]) & 1
        x = self._state[0]
        self._state = self._state[1:] + [f]
        return x

def LFSR_matrix(size, taps):
    m = []
    for i in range(size - 1):
        m.append([0] * size)
        m[i][i + 1] = 1
    m.append([0] * size)
    for i in taps:
        m[size - 1][i] = 1
    return m


def exponentiate_by_squaring(base, exponent):
    if exponent == 0:
        return 1
    elif exponent % 2 == 0:
        # If the exponent is even, use the property a^(2n) = (a^n)^2
        temp = exponentiate_by_squaring(base, exponent // 2)
        return temp * temp
    else:
        # If the exponent is odd, use the property a^(2n+1) = a * (a^n)^2
        temp = exponentiate_by_squaring(base, (exponent - 1) // 2)
        return base * temp * temp


flag = list(map(int, ''.join(["{:08b}".format(c) for c in FLAG])))
key =  list(map(int, ''.join(["{:08b}".format(c) for c in urandom(8)])))
key = [1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1]
taps = [0, 2, 17, 19, 23, 37, 41, 53]
randomness = LFSR(taps, key)
print("key:",key)
v = vector(key)
v2 = vector(key)
v3 = vector(key)
m = Matrix(Integers(2), LFSR_matrix(64, taps))

output = []
for _ in range(len(flag) + 70):
    for __ in range(70):
        randomness.getbit()
    output.append(randomness.getbit())

output2 = []
for _ in range(len(flag) + 70):
    for __ in range(70):
        v = m * v
    output2.append(int(v[0]))
    v = m * v

output3 = []
m_70 = exponentiate_by_squaring(m, 70)
for _ in range(len(flag) + 70):
    v2 = m_70 * v2
    output3.append(int(v2[0]))
    v2 = m * v2

output4 = []
m_71_256 = exponentiate_by_squaring(m_70 * m, len(flag))
#v3 = m_71_256 * v3
target = []
M = m_71_256
for i in range(70):
    #v3 = m_70 * v3
    M *= m_70
    if i < 64:
        target.append(list(M[63]))
    output4.append(int((M * v3)[0]))
    #v3 = m * v3
    M *= m
print("Target")
print(target)
print()
target = Matrix(Integers(2), target)
print("Oringin")
print(target)

print(v2[-70:])
print(M * v3)
print(v2[-70:] == M * v3)

for i in range(len(flag)):
    output[i] ^= flag[i]

for i in range(len(flag)):
    output2[i] ^= flag[i]

for i in range(len(flag)):
    output3[i] ^= flag[i]

print(output)
print(output2)
print(output3)
print(output == output2)
print(output2 == output3)
# [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0]