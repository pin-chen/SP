#!/usr/bin/env python
import itertools
from Crypto.Util.number import long_to_bytes

class LFSR:
    def __init__(self, tap, state):
        self._tap = tap
        self._state = state

    def getbit(self):
        f = sum([self._state[i] for i in self._tap]) & 1
        x = self._state[0]
        self._state = self._state[1:] + [f]
        return x

from tqdm import tqdm
def correlation_attack(stream, key_len):
    for b in tqdm(range(key_len)):
        for c in itertools.combinations(range(key_len), b):
            key_candidate = [1 - stream[i] if i in c else stream[i] for i in range(key_len)]
            lfsr = LFSR([0, 1, 2, 5], key_candidate)
            s = [lfsr.getbit() for _ in range(200)]
            matches = sum(a == b for a, b in zip(stream, s))
            if(matches >= 140):
                print(key_candidate)
                return key_candidate
    
stream = [0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0]

key2 = correlation_attack(stream, 23)
key3 = correlation_attack(stream, 27)

lfsr2 = LFSR([0, 1, 2, 5], key2)
lfsr3 = LFSR([0, 1, 2, 5], key3)

lfsr2_steam = [lfsr2.getbit() for _ in stream]
lfsr3_steam = [lfsr3.getbit() for _ in stream]

flag = []
for k in tqdm(range(1 << 19)):
    key_candidate = list(map(int, bin(k)[2:].rjust(19, '0')))
    lfsr = LFSR([0, 1, 2, 5], key_candidate)
    suc = True
    for i in range(200):
        if(lfsr2_steam[i] if lfsr.getbit() else lfsr3_steam[i]) != stream[i]:
            suc = False
            break 

    if suc:
        key_candidate = list(map(int, bin(k)[2:].rjust(19, '0')))
        print(key_candidate)
        lfsr = LFSR([0, 1, 2, 5], key_candidate)
        for i, s in enumerate(stream):
            flag.append(s ^ (lfsr2_steam[i] if lfsr.getbit() else lfsr3_steam[i]))

print(long_to_bytes(int("".join(map(str, flag[200:])), 2)).decode())