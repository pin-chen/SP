#!/usr/bin/env python
from pwn import *
from Crypto.Util.number import long_to_bytes, bytes_to_long, getPrime
from Crypto.Cipher import AES
from random import randbytes

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

N = 69214008498642035761243756357619851816607540327248468473247478342523127723748756926949706235406640562827724567100157104972969498385528097714986614165867074449238186426536742677816881849038677123630836686152379963670139334109846133566156815333584764063197379180877984670843831985941733688575703811651087495223
e = 65537
encrypted_key = 65690013242775728459842109842683020587149462096059598501313133592635945234121561534622365974927219223034823754673718159579772056712404749324225325531206903216411508240699572153162745754564955215041783396329242482406426376133687186983187563217156659178000486342335478915053049498619169740534463504372971359692
encrypted_iv = 35154524936059729204581782839781987236407179504895959653768093617367549802652967862418906182387861924584809825831862791349195432705129622783580000716829283234184762744224095175044663151370869751957952842383581513986293064879608592662677541628813345923397286253057417592725291925603753086190402107943880261658
encrypted_flag = open('chall/encrypted_flag.not_png', 'rb').read()

r = remote('10.113.184.121', 10031)

r.sendlineafter(b'key: ', str(encrypted_key).encode())
r.sendlineafter(b'iv: ', str(encrypted_iv).encode())
r.sendlineafter(b'ciphertext: ', encrypted_flag.hex().encode())
assert r.recvline() == b'OK! Got it.\n'

def send_to_check(key, iv, ct):
    r.sendlineafter(b'key: ', str(key).encode())
    r.sendlineafter(b'iv: ', str(iv).encode())
    r.sendlineafter(b'ciphertext: ', ct.hex().encode())
    return r.recvline() == b'OK! Got it.\n'

fake_aes_key = b'\x00'*14 + b'\x12' + b'\x13'
fake_flag = b'\x00' * 16

iv, ct = symmetric_encryption(fake_flag, fake_aes_key)
fake_encrypted_key = asymmetric_encryption(fake_aes_key, N, e)
fake_encrypted_iv = asymmetric_encryption(iv, N, e)
assert send_to_check(fake_encrypted_key, fake_encrypted_iv, ct) == True

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

key = POA(encrypted_key)
iv = POA(encrypted_iv)

print('key: ', key)
print('iv: ', iv)

cipher = AES.new(key, AES.MODE_CBC, iv)
open('flag.png', 'wb').write(unpad(cipher.decrypt(encrypted_flag)))
