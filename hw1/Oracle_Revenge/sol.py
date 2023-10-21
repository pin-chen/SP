#!/usr/bin/env python
from pwn import *
from Crypto.Util.number import long_to_bytes, bytes_to_long
from Crypto.Cipher import AES
from random import randbytes

r = remote('10.113.184.121', 10031)

def pad(m):
    length = 16-len(m) % 16
    return m + chr(length).encode()*length

def unpad(c):
    length = c[-1]
    for char in c[-length:]:
        if char != length:
            raise ValueError
    return c[:-length]

def asymmetric_encryption(message, N, e):
    # encrypt message with RSA
    # message must be 16 bytes
    # padding 100 bytes random value
    padded_message = randbytes(100) + message
    return pow(bytes_to_long(padded_message), e, N)

def symmetric_encryption(message, key):
    # ecrypt message with AES + CBC Mode
    # message can be arbitrary length
    cipher = AES.new(key, AES.MODE_CBC)
    ct = cipher.encrypt(pad(message))
    iv = cipher.iv
    return iv, ct

def no_pad_symmetric_encryption(message, key):
    # ecrypt message with AES + CBC Mode
    # message can be arbitrary length
    cipher = AES.new(key, AES.MODE_CBC, b'\x00'*16)
    ct = cipher.encrypt(message)
    iv = cipher.iv
    return iv, ct

def send_to_check(key, iv, ct):
    r.sendlineafter(b'key: ', str(key).encode())
    r.sendlineafter(b'iv: ', str(iv).encode())
    r.sendlineafter(b'ciphertext: ', ct.hex().encode())
    return r.recvline() == b'OK! Got it.\n'

def POA(encrypted_target, key=b'\x00'*16):
    result = []
    assert len(key) == 16
    encrypted_key = asymmetric_encryption(key, N, e)
    for i in range(16):
        tmp = b''
        for j in range(i):
            tmp += bytes([result[i - j - 1] ^ (i + 1)])
        for c in range(256):
            fake_flag = b'\x00' * (15 - i) + bytes([c]) + tmp
            _, ct = no_pad_symmetric_encryption(fake_flag, key)
            if send_to_check(encrypted_key, encrypted_target, ct) == True:
                result.append(c ^ (i + 1))
                break
        assert len(result) == i + 1
    return bytes(reversed(result))

encrypted_flag = 67448907891721241368838325896320122397092733550961191069708016032244349188684070793897519352151466622385197077064799553157879456334546372809948272281247935498288157941438709402245513879910090372080411345199729220479271018326225319584057160895804120944126979515126944833368164622466123481816185794224793277249
N = 69214008498642035761243756357619851816607540327248468473247478342523127723748756926949706235406640562827724567100157104972969498385528097714986614165867074449238186426536742677816881849038677123630836686152379963670139334109846133566156815333584764063197379180877984670843831985941733688575703811651087495223
e = 65537

mod = pow(0x100, 16)
mod_inv = pow(mod, -1, N)
mod_inv_e = pow(mod, -e, N)
remainder = 0
flag = b''
while True:
    print('.', end='')
    ret = POA(encrypted_flag)
    x = bytes_to_long(ret)
    x = (x - remainder) % mod
    flag = long_to_bytes(x) + flag
    if b'FLAG{' in flag:
        break
    encrypted_flag = encrypted_flag * mod_inv_e % N
    remainder = (remainder + x) * mod_inv % N
    
print('\nFLAG' + flag.split(b'FLAG')[1].decode())