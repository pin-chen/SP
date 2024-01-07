
from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes as l2b, bytes_to_long as b2l
FLAG=b'flag{xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx}'
from os import urandom
from base64 import b64encode, b64decode

from pwn import *

#c1_CFB: (b'ujPULsJp7eDHQQZc0NHpQQ==', b'fAfaWX7j60ZiPNdW+rVoIgHDKMAu0lVFkqn+yLE5aKE=')
#c2_OFB: (b'ujPULsJp7eDHQQZc0NHpQg==', b'OM7PfGfCS813X7vvn3WObgs8WP2G6mTH2as/O2GnJWo=')
#c3_CTR: (b'ujPULsJp7eDHQQZc0NHpQw==', b'6yCVJLjuQ+TRd4N5IQ67EvEgt2t+9CL6S0FxMbdifps=')


#c1_CFB: (b'0oo8JBhO0VrzuZ1iB94fdw==', b'ndRYZqQwLleb/mPrWvGLW4/Ye8ssIW/Md3z7W1ziu8M=')
#c2_OFB: (b'0oo8JBhO0VrzuZ1iB94feA==', b'zGOv36H/inzlMqMKYdX7qFCqylVsIit70i89ts5/qqg=')
#c3_CTR: (b'0oo8JBhO0VrzuZ1iB94feQ==', b'c1B5bQ27+hGmGZzRwsqARkp7rCrHi1Pr8E6ZcmOXK80=')


r = remote('chal1.eof.ais3.org', 10003)

#
#
#r = process(['python3', 'release/AES.py'])

#
#
debug = 0

x = r.recvuntil(b'c1_CFB: (b\'')

print(x.decode())

iv_cfb = r.recvuntil(b'\'').split(b'\'')[0]
r.recvuntil(b', b\'')
ct_cfb = r.recvuntil(b'\'').split(b'\'')[0]
if debug:
    r.recvuntil(b'A: b\'')
    x = r.recvuntil(b'\'')
    print("-------", x)

r.recvuntil(b'c2_OFB: (b\'')
iv_ofb = r.recvuntil(b'\'').split(b'\'')[0]
r.recvuntil(b', b\'')
ct_ofb = r.recvuntil(b'\'').split(b'\'')[0]
r.recvuntil(b'c3_CTR: (b\'')
iv_ctr = r.recvuntil(b'\'').split(b'\'')[0]
r.recvuntil(b', b\'')
ct_ctr = r.recvuntil(b'\'').split(b'\'')[0]
#r.recvuntil(b'What operation mode do you want for encryption? ')


iv_cfb = b64decode(iv_cfb)
ct_cfb = b64decode(ct_cfb)
iv_ofb = b64decode(iv_ofb)
ct_ofb = b64decode(ct_ofb)


iv_ctr = b64decode(iv_ctr)
ct_ctr = b64decode(ct_ctr)

print(iv_cfb)
print(ct_cfb)
print(iv_ofb)
print(ct_ofb)
print(iv_ctr)
print(ct_ctr)

def XOR (a, b):
    return l2b(b2l(a) ^ b2l(b)).rjust(len(a), b"\x00")
    
def counter_add(iv):
    return l2b(b2l(iv) + 1).rjust(16, b"\x00")

def AES(pt, mode):
    r.recvuntil(b'What operation mode do you want for encryption? ')
    r.sendline(mode.encode())
    r.recvuntil(b'What message do you want to encrypt (in base64)? ')
    r.sendline(b64encode(pt))
    
    r.recvuntil(b'b\'')
    iv = r.recvuntil(b'\'').split(b'\'')[0]
    r.recvuntil(b' b\'')
    ct = r.recvuntil(b'\'').split(b'\'')[0]
    if mode == 'CTR' and debug:
        for i in range(5):
            r.recvuntil(b'A: b\'')
            x = r.recvuntil(b'\'')
            print("-------", x)
    return b64decode(iv), b64decode(ct)

magic_null_pt = b'\x00'*16*5
print("------------------")
print(magic_null_pt)
iv, magic_ct = AES(magic_null_pt, 'CTR')
print(magic_ct[0:16])
print(magic_ct[16:32]) #next1
print(magic_ct[32:48]) #next2
print(magic_ct[48:64]) #next3
print(magic_ct[64:80]) #next4

magic_iv_geter = XOR(magic_ct[16:32], iv_cfb) + b'\x00'*16
iv, ct = AES(magic_iv_geter, 'CFB')
aes_cfb_iv = ct[16:32]
#print(aes_cfb_iv)
pt = XOR(ct_cfb[0:16], aes_cfb_iv)
#print(pt)
next_needed_iv = ct_cfb[0:16]
magic_iv_geter = XOR(magic_ct[32:48], next_needed_iv) + b'\x00'*16
iv, ct = AES(magic_iv_geter, 'CFB')
aes_cfb_iv = ct[16:32]
#print(aes_cfb_iv)
pt += XOR(ct_cfb[16:32], aes_cfb_iv)
#print(pt)

c1 = pt
print("c1:",c1)

# -------------------------------
magic_iv_geter = XOR(magic_ct[48:64], iv_ofb) + b'\x00'*16
iv, ct = AES(magic_iv_geter, 'CFB')
aes_ofb_iv = ct[16:32]
#print(aes_ofb_iv)
pt = XOR(ct_ofb[0:16], aes_ofb_iv)
#print(pt)
'''
next_needed_iv = aes_ofb_iv
magic_iv_geter = XOR(magic_ct[64:80], next_needed_iv) + b'\x00'*16
iv, ct = AES(magic_iv_geter, 'CFB')
aes_ofb_iv = ct[16:32]
#print(aes_ofb_iv)
pt += XOR(ct_ofb[16:32], aes_ofb_iv)
#print(pt)
'''
c2 = pt
print("c2:",c2)

#------------------------
magic_iv_geter = XOR(magic_ct[64:80], iv_ctr) + b'\x00'*16
iv, ct = AES(magic_iv_geter, 'CFB')
aes_ctr_iv = ct[16:32]
print(aes_ctr_iv)

c3_1 = XOR(ct_ctr[0:16], aes_ctr_iv)
print(c3_1)
tmp = XOR(c1[0:16], c2[0:16])
flag = XOR(c3_1, tmp)
print(flag)

exit()
#------------------------
tmp = XOR(c1, c2)
print(len(tmp))
print(len(c1))
print(len(c2))

print(len(ct_ctr))


c3_2 = XOR(magic_ct[0:16], ct_ctr[16:32]) 
#c3_3 = XOR(magic_ct[16:32], ct_ctr[32:48])
#c3_2 = XOR(magic_ct[0:16], ct_ctr[48:64]) 
#c3_3 = XOR(magic_ct[16:32], ct_ctr[64:80])
print(c3_2)
#print(c3_3)

c3 = XOR(c3_2, tmp[16:32])
print("c3:",c3)
"""
c3 = XOR(c3_3, tmp)
print("c3:",c3)
c3 = XOR(c3_2+c3_3, tmp)
print("c3:",c3)
"""
#c3: b'\x9f\x16\xecfT\xdcSs\x1bj\xec\xcf\xdfu\x85\x81
#AIS3{_Bl0ck_C1Ph3R_m0de_MaStER_}
#{xxxxxxxxxxxxxx}
r.interactive()
exit(0)

#iv, ct = AES(iv_cfb, 'CFB')
print("------------------")
iv, ct = AES(iv_ofb, 'OFB')
aes_iv_1 = XOR(iv_ofb, ct)
print(iv, aes_iv_1)

iv, ct = AES(iv_ofb, 'OFB')
aes_iv_2 = XOR(iv_ofb, ct)
print(iv, aes_iv_2)

iv, ct = AES(iv_ofb, 'OFB')
aes_iv_3 = XOR(iv_ofb, ct)
print(iv, aes_iv_3)

iv, ct = AES(iv_ofb, 'OFB')
aes_iv_4 = XOR(iv_ofb, ct)
print(iv, aes_iv_4)

iv, ct = AES(iv_ofb, 'OFB')
aes_iv_5 = XOR(iv_ofb, ct)
print(iv, aes_iv_5)

#cfb
"""
iv, ct = AES(iv_cfb, 'OFB')
aes_iv_cfb = XOR(iv, ct)
pt = XOR(aes_iv_cfb, ct_cfb[0:16])
print(pt)
iv, ct = AES(ct_cfb[0:16], 'OFB')
aes_iv_cfb = XOR(iv, ct)
pt += XOR(aes_iv_cfb, ct_cfb[16:32])
print(pt)
"""


print("-------")

print(XOR(ct_ctr[16:32], aes_iv_1))
print(XOR(ct_ctr[32:48], aes_iv_2))
print(XOR(ct_ctr[48:64], aes_iv_3))
print(XOR(ct_ctr[64:80], aes_iv_4))
print(XOR(ct_ctr[80:96], aes_iv_5))






#CTR
#AES(counter) xor c3[0:16]
#AES(counter+1) xor c3[16:32] = ct_ctr[16:32]
#AES(counter+2) xor c3[32:48] = ct_ctr[32:48]
#AES(counter+3) xor c3[48:64] = ct_ctr[48:64]
#AES(counter+4) xor c3[64:80] = ct_ctr[64:80]
#AES(counter+5) xor c3[80:96] = ct_ctr[80:96]

#known
#AES(counter+1) -> c3[16:32]
#AES(counter+2) -> c3[32:48]
#AES(counter+3) -> c3[48:64]
#AES(counter+4) -> c3[64:80]
#AES(counter+5) -> c3[80:96]

#CFB
#iv, pt