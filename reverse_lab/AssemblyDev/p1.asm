;let a = MEM[RSP+0x0:RSP+0x4]
;let b = MEM[RSP+0x4:RSP+0x8]
mov r8d, dword [rsp+0x0]
mov r9d, dword [rsp+0x4]
;EAX = a + b
mov eax, r8d
add eax, r9d
;EBX = a - b
mov ebx, r8d
sub ebx, r9d
;let c = MEM[RSP+0x8:RSP+0xc]
;ECX = -c
mov ecx, dword [rsp+0x8]
neg ecx
;EDX = 9*a + 7
mov edx, r8d
imul edx, 0x9
add edx, 0x7