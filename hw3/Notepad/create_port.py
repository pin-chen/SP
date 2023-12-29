from pwn import *
import subprocess

def create_port():
    r = remote('10.113.184.121', 10044)

    r.recvuntil(b'sha256(')
    prefix = r.recvuntil(b' +')[0:-2].decode()
    r.recvuntil(b'(')
    difficulty = r.recvuntil(b')')[0:-1].decode()
    r.recvuntil(b"Answer: ")

    result = subprocess.run(['release/pow_solver.py', prefix, difficulty], stdout=subprocess.PIPE, text=True)

    print("pow:", result.stdout)

    r.sendline(result.stdout.encode())
    r.recvuntil(b'port ')
    port = int(r.recvuntil(b'.')[0:-1].decode())
    r.close()
    print("port", port)
    return port

if __name__ == '__main__':
    create_port()