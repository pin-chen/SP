#!/usr/bin/env bash
"sage" "--python" "$0"
"exit" "$?"

from Crypto.Util.number import bytes_to_long, long_to_bytes
from os import urandom
from sage.all import *
from z3 import *
from tqdm import tqdm
from collections import deque
# Target cipher 
#stream = [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0]
# Test chpher
stream = [0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1]
# Generate LFSR matrix
def LFSR_matrix(size, taps):
    m = []
    for i in range(size - 1):
        m.append([0] * size)
        m[i][i + 1] = 1
    m.append([0] * size)
    for i in taps:
        m[size - 1][i] = 1
    return m
# LFSR
class LFSR:
    def __init__(self, tap, state):
        self._tap = tap
        self._state = state

    def getbit(self):
        f = sum([self._state[i] for i in self._tap]) & 1
        x = self._state[0]
        self._state = self._state[1:] + [f]
        return x
# exponentiate_by_squaring
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
    
def sum_queue_elements(queue):
    while len(queue) >= 2:
        # Dequeue the first two elements
        element1 = queue.popleft()
        element2 = queue.popleft()
        # Add them together
        sum_of_elements = Xor(element1, element2)
        # Enqueue the result back into the queue
        queue.append(sum_of_elements)
    if len(queue) >= 0:
        return queue.popleft()
    else:
        return None

# taps
taps = [0, 2, 17, 19, 23, 37, 41, 53]
# get LFSR matrix with sage Matrix
m = Matrix(Integers(2), LFSR_matrix(64, taps))
# 後70沒有與 plantext xor
stream, hint = stream[:-70], stream[-70:]
# plantext bit length
print(len(stream))
# LFSR Matrix ^ 70
m_70 = exponentiate_by_squaring(m, 70)
print(m_70)
print()
# LFSR Matrix ^ (71 * len(stream))
m_71_256 = exponentiate_by_squaring(m_70 * m, len(stream))
print(m_71_256)
# z3 SAT solver
solver = Solver()
# 64 variables
x = [Bool(f'x{i}') for i in range(64)]
# 前綴 "FLAG{" 為已知可求得原本的樣貌
prev = list(map(int, ''.join(["{:08b}".format(c) for c in b"FLAG{"])))
for i in range(len(prev)):
    prev[i] = (prev[i] + stream[i]) & 1
#print(prev)
# 生前綴 40 條 equation
M = m
for i in tqdm(range(0)):
    #equation = False
    queue = deque()
    M *= m_70
    for j in range(64):
        val = M[63][j]
        if val == 1:
            queue.append(x[j])
            #equation = Xor(equation, x[j])
    equation = sum_queue_elements(queue)
    solver.add(equation == bool(prev[i]))
    M *= m
# 生後 70 條 equation 
M = m_71_256
for i in tqdm(range(70)):
    #equation = False
    queue = deque()
    M *= m_70
    for j in range(64):
        val = M[63][j]
        if val == 1:
            queue.append(x[j])
            #equation = Xor(equation, x[j])
    equation = sum_queue_elements(queue)
    solver.add(equation == bool(hint[i]))
    M *= m
# z3 solver 解
key = []
print("Checking")
if solver.check() == sat:
    print("Checked")
    model = solver.model()
    for i, var in enumerate(x):
        value = model[var]
        #print(f"x[{i}] = {value}")
        if value:
            key.append(1)
        else:
            key.append(0)
else:
    print("No satisfying assignment found.")
# key value
print(key)
# Get plantext
v = vector(key)
output3 = []
for _ in range(len(stream)):
    v = m_70 * v
    output3.append(int(v[0]))
    v = m * v

for i in range(len(stream)):
    output3[i] = (output3[i] + stream[i]) & 1

print(long_to_bytes(int("".join(map(str, output3)), 2)))



#with open('z3.py','w') as file:
#print('from z3 import *', file=file)
#print('solver = Solver()', file=file)
    #print("solver.add(Xor(", end='', file=file)
            #print(f"x[{j}]",end=',', file=file)
    #print(hint[i], ") == 0 )", file=file)

'''print("""if solver.check() == sat:
model = solver.model()
    
    # Access and print the values of the Boolean variables
    for i, var in enumerate(variables):
        value = model[var]
        print(f"x[{i}] = {value}")
else:
    print("No satisfying assignment found.")""", file=file)'''

"""
v = vector([0] * 64)
v[0] = hint[-1]
v2 = m.inverse() * v1
t = [0] * 63
v1 = [hint[-1], t[0], t[1], t[2],...]
v2 = [t[0], t[1], t[2],...]
sum(t[taps]) & 1 = hint[-1]

m ^ -70 * v2 = [hint[-2], t1[0], t1[1],...]
m ^ -71 * v2 = [t1[0], t1[1],...]
sum(t1[taps] & 1 ) == hint[-2]
"""

"""
for k in range(1 << 63):
    if(k % 1000 == 0):
        print(k)
    key_candidate = list(map(int, bin(k)[2:].rjust(63, '0')))
    if sum([key_candidate[i] for i in taps]) & 1 != hint[-1]:
        continue
    key_candidate = vector([hint[-1]] + key_candidate)
    suc = True
    for i in range(69):
        for _ in range(70):
            key_candidate = m.inverse() * key_candidate
        if key_candidate[0] != hint[-(i + 2)]:
            suc = False
            break
        key_candidate = m.inverse() * key_candidate
    if suc:
        key_candidate = list(map(int, bin(k)[2:].rjust(63, '0')))
        print(hint[-1] + key_candidate)
"""