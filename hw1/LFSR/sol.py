#!/usr/bin/env bash
"sage" "--python" "$0"
"exit" "$?"

from Crypto.Util.number import long_to_bytes
from sage.all import *

hint = [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0]
taps = [0, 2, 17, 19, 23, 37, 41, 53]


# Generate a shift matrix and change the last row to "taps"
def generate_shift_matrix(size, taps):
    result = []
    for i in range(size - 1):
        result.append([0] * size)
        result[i][i + 1] = 1
    result.append([0] * size)
    for i in taps:
        result[size - 1][i] = 1
    return Matrix(Integers(2), result)


# Exponentiation by squaring
def exponentiation_by_squaring(base, exponent):
    if exponent == 0:
        return 1
    elif exponent % 2 == 0:
        temp = exponentiation_by_squaring(base, exponent // 2)
        return temp * temp
    else:
        temp = exponentiation_by_squaring(base, (exponent - 1) // 2)
        return base * temp * temp


# key is 64 bit since urandom(8) (8 bytes * 8 = 64 bits)
m = generate_shift_matrix(64, taps)
# Get a matrix can skip 70 times getbit
m_70 = exponentiation_by_squaring(m, 70)
# Get a matrix cam skip previous 256 hints about flag
M = exponentiation_by_squaring(m * m_70, len(hint) - 70)
# Get 64 rows about hint[256:256+64]
target = []
for i in range(64):
    M *= m_70
    target.append(M.row(0))
    M *= m
# Covert to Matrix in sage
target = Matrix(Integers(2), target)
# Let hint[256:256+64] be 1 x 64 column
col = Matrix([[val] for val in hint[-70 : -70 + 64]])
# Combine
target = target.augment(col, subdivide=True)
# Gaussian Elimination
target = target.echelon_form()
# Get key
key = target.column(-1)
# Do it again
flag = []
for _ in range(256):
    key = m_70 * key
    flag.append(int(key[0]))
    key = m * key
# Xor with hint
for i in range(256):
    flag[i] = (flag[i] + hint[i]) & 1
# Get flag
print(long_to_bytes(int("".join(map(str, flag)), 2)).decode())
