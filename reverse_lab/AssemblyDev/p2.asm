;RAX += 0x87
add rax, 0x87
;RBX -= 0x63
sub rbx, 0x63
;RCX, RDX = RDX, RCX
mov rdi, rdx
mov rdx, rcx
mov rcx, rdi
;MEM[RSP+0x0:RSP+0x4] += 0xdeadbeef
mov r8d, dword [rsp]
add r8d, 0xdeadbeef
mov [rsp], r8d
;MEM[RSP+0x4:RSP+0x8] -= 0xfaceb00c
mov r8d, dword [rsp+4]
sub r8d, 0xfaceb00c
mov [rsp+0x4], r8d
;MEM[RSP+0x8:RSP+0xc], MEM[RSP+0xc:RSP+0x10] = MEM[RSP+0xc:RSP+0x10], MEM[RSP+0x8:RSP+0xc]
mov r8d, dword [rsp+0x8]
mov r9d, dword [rsp+0xc]
mov [rsp+0x8], r9d
mov [rsp+0xc], r8d