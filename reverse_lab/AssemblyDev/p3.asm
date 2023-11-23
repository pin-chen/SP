Q1:
	mov r8d, dword [rsp+0x0]
	mov r9d, dword [rsp+0x4]
	cmp r8d, r9d
	jge EAX_a
EAX_b:
	mov eax, r9d
	jmp Q2
EAX_a:
	mov eax, r8d
Q2:
	mov r8d, dword [rsp+0x8]
	mov r9d, dword [rsp+0xc]
	cmp r8d, r9d
	jb EBX_c
EBX_d:
	mov ebx, r9d
	jmp Q3
EBX_c:
	mov ebx, r8d
Q3:
	mov ecx, r8d
	test r8d, 0x1
	jnz odd
even:
	mov ecx, r8d
	shl ecx, 0x2
	jmp fin
odd:
	shr ecx, 0x3
fin: