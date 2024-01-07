
share/jackpot:     file format elf64-x86-64


Disassembly of section .init:

0000000000401000 <_init>:
  401000:	f3 0f 1e fa          	endbr64 
  401004:	48 83 ec 08          	sub    rsp,0x8
  401008:	48 8b 05 e9 2f 00 00 	mov    rax,QWORD PTR [rip+0x2fe9]        # 403ff8 <__gmon_start__@Base>
  40100f:	48 85 c0             	test   rax,rax
  401012:	74 02                	je     401016 <_init+0x16>
  401014:	ff d0                	call   rax
  401016:	48 83 c4 08          	add    rsp,0x8
  40101a:	c3                   	ret    

Disassembly of section .plt:

0000000000401020 <.plt>:
  401020:	ff 35 e2 2f 00 00    	push   QWORD PTR [rip+0x2fe2]        # 404008 <_GLOBAL_OFFSET_TABLE_+0x8>
  401026:	f2 ff 25 e3 2f 00 00 	bnd jmp QWORD PTR [rip+0x2fe3]        # 404010 <_GLOBAL_OFFSET_TABLE_+0x10>
  40102d:	0f 1f 00             	nop    DWORD PTR [rax]
  401030:	f3 0f 1e fa          	endbr64 
  401034:	68 00 00 00 00       	push   0x0
  401039:	f2 e9 e1 ff ff ff    	bnd jmp 401020 <_init+0x20>
  40103f:	90                   	nop
  401040:	f3 0f 1e fa          	endbr64 
  401044:	68 01 00 00 00       	push   0x1
  401049:	f2 e9 d1 ff ff ff    	bnd jmp 401020 <_init+0x20>
  40104f:	90                   	nop
  401050:	f3 0f 1e fa          	endbr64 
  401054:	68 02 00 00 00       	push   0x2
  401059:	f2 e9 c1 ff ff ff    	bnd jmp 401020 <_init+0x20>
  40105f:	90                   	nop
  401060:	f3 0f 1e fa          	endbr64 
  401064:	68 03 00 00 00       	push   0x3
  401069:	f2 e9 b1 ff ff ff    	bnd jmp 401020 <_init+0x20>
  40106f:	90                   	nop
  401070:	f3 0f 1e fa          	endbr64 
  401074:	68 04 00 00 00       	push   0x4
  401079:	f2 e9 a1 ff ff ff    	bnd jmp 401020 <_init+0x20>
  40107f:	90                   	nop
  401080:	f3 0f 1e fa          	endbr64 
  401084:	68 05 00 00 00       	push   0x5
  401089:	f2 e9 91 ff ff ff    	bnd jmp 401020 <_init+0x20>
  40108f:	90                   	nop
  401090:	f3 0f 1e fa          	endbr64 
  401094:	68 06 00 00 00       	push   0x6
  401099:	f2 e9 81 ff ff ff    	bnd jmp 401020 <_init+0x20>
  40109f:	90                   	nop
  4010a0:	f3 0f 1e fa          	endbr64 
  4010a4:	68 07 00 00 00       	push   0x7
  4010a9:	f2 e9 71 ff ff ff    	bnd jmp 401020 <_init+0x20>
  4010af:	90                   	nop

Disassembly of section .plt.sec:

00000000004010b0 <puts@plt>:
  4010b0:	f3 0f 1e fa          	endbr64 
  4010b4:	f2 ff 25 5d 2f 00 00 	bnd jmp QWORD PTR [rip+0x2f5d]        # 404018 <puts@GLIBC_2.2.5>
  4010bb:	0f 1f 44 00 00       	nop    DWORD PTR [rax+rax*1+0x0]

00000000004010c0 <printf@plt>:
  4010c0:	f3 0f 1e fa          	endbr64 
  4010c4:	f2 ff 25 55 2f 00 00 	bnd jmp QWORD PTR [rip+0x2f55]        # 404020 <printf@GLIBC_2.2.5>
  4010cb:	0f 1f 44 00 00       	nop    DWORD PTR [rax+rax*1+0x0]

00000000004010d0 <read@plt>:
  4010d0:	f3 0f 1e fa          	endbr64 
  4010d4:	f2 ff 25 4d 2f 00 00 	bnd jmp QWORD PTR [rip+0x2f4d]        # 404028 <read@GLIBC_2.2.5>
  4010db:	0f 1f 44 00 00       	nop    DWORD PTR [rax+rax*1+0x0]

00000000004010e0 <prctl@plt>:
  4010e0:	f3 0f 1e fa          	endbr64 
  4010e4:	f2 ff 25 45 2f 00 00 	bnd jmp QWORD PTR [rip+0x2f45]        # 404030 <prctl@GLIBC_2.2.5>
  4010eb:	0f 1f 44 00 00       	nop    DWORD PTR [rax+rax*1+0x0]

00000000004010f0 <setvbuf@plt>:
  4010f0:	f3 0f 1e fa          	endbr64 
  4010f4:	f2 ff 25 3d 2f 00 00 	bnd jmp QWORD PTR [rip+0x2f3d]        # 404038 <setvbuf@GLIBC_2.2.5>
  4010fb:	0f 1f 44 00 00       	nop    DWORD PTR [rax+rax*1+0x0]

0000000000401100 <perror@plt>:
  401100:	f3 0f 1e fa          	endbr64 
  401104:	f2 ff 25 35 2f 00 00 	bnd jmp QWORD PTR [rip+0x2f35]        # 404040 <perror@GLIBC_2.2.5>
  40110b:	0f 1f 44 00 00       	nop    DWORD PTR [rax+rax*1+0x0]

0000000000401110 <__isoc99_scanf@plt>:
  401110:	f3 0f 1e fa          	endbr64 
  401114:	f2 ff 25 2d 2f 00 00 	bnd jmp QWORD PTR [rip+0x2f2d]        # 404048 <__isoc99_scanf@GLIBC_2.7>
  40111b:	0f 1f 44 00 00       	nop    DWORD PTR [rax+rax*1+0x0]

0000000000401120 <exit@plt>:
  401120:	f3 0f 1e fa          	endbr64 
  401124:	f2 ff 25 25 2f 00 00 	bnd jmp QWORD PTR [rip+0x2f25]        # 404050 <exit@GLIBC_2.2.5>
  40112b:	0f 1f 44 00 00       	nop    DWORD PTR [rax+rax*1+0x0]

Disassembly of section .text:

0000000000401130 <_start>:
  401130:	f3 0f 1e fa          	endbr64 
  401134:	31 ed                	xor    ebp,ebp
  401136:	49 89 d1             	mov    r9,rdx
  401139:	5e                   	pop    rsi
  40113a:	48 89 e2             	mov    rdx,rsp
  40113d:	48 83 e4 f0          	and    rsp,0xfffffffffffffff0
  401141:	50                   	push   rax
  401142:	54                   	push   rsp
  401143:	45 31 c0             	xor    r8d,r8d
  401146:	31 c9                	xor    ecx,ecx
  401148:	48 c7 c7 c7 12 40 00 	mov    rdi,0x4012c7
  40114f:	ff 15 9b 2e 00 00    	call   QWORD PTR [rip+0x2e9b]        # 403ff0 <__libc_start_main@GLIBC_2.34>
  401155:	f4                   	hlt    
  401156:	66 2e 0f 1f 84 00 00 	cs nop WORD PTR [rax+rax*1+0x0]
  40115d:	00 00 00 

0000000000401160 <_dl_relocate_static_pie>:
  401160:	f3 0f 1e fa          	endbr64 
  401164:	c3                   	ret    
  401165:	66 2e 0f 1f 84 00 00 	cs nop WORD PTR [rax+rax*1+0x0]
  40116c:	00 00 00 
  40116f:	90                   	nop

0000000000401170 <deregister_tm_clones>:
  401170:	b8 80 41 40 00       	mov    eax,0x404180
  401175:	48 3d 80 41 40 00    	cmp    rax,0x404180
  40117b:	74 13                	je     401190 <deregister_tm_clones+0x20>
  40117d:	b8 00 00 00 00       	mov    eax,0x0
  401182:	48 85 c0             	test   rax,rax
  401185:	74 09                	je     401190 <deregister_tm_clones+0x20>
  401187:	bf 80 41 40 00       	mov    edi,0x404180
  40118c:	ff e0                	jmp    rax
  40118e:	66 90                	xchg   ax,ax
  401190:	c3                   	ret    
  401191:	66 66 2e 0f 1f 84 00 	data16 cs nop WORD PTR [rax+rax*1+0x0]
  401198:	00 00 00 00 
  40119c:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]

00000000004011a0 <register_tm_clones>:
  4011a0:	be 80 41 40 00       	mov    esi,0x404180
  4011a5:	48 81 ee 80 41 40 00 	sub    rsi,0x404180
  4011ac:	48 89 f0             	mov    rax,rsi
  4011af:	48 c1 ee 3f          	shr    rsi,0x3f
  4011b3:	48 c1 f8 03          	sar    rax,0x3
  4011b7:	48 01 c6             	add    rsi,rax
  4011ba:	48 d1 fe             	sar    rsi,1
  4011bd:	74 11                	je     4011d0 <register_tm_clones+0x30>
  4011bf:	b8 00 00 00 00       	mov    eax,0x0
  4011c4:	48 85 c0             	test   rax,rax
  4011c7:	74 07                	je     4011d0 <register_tm_clones+0x30>
  4011c9:	bf 80 41 40 00       	mov    edi,0x404180
  4011ce:	ff e0                	jmp    rax
  4011d0:	c3                   	ret    
  4011d1:	66 66 2e 0f 1f 84 00 	data16 cs nop WORD PTR [rax+rax*1+0x0]
  4011d8:	00 00 00 00 
  4011dc:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]

00000000004011e0 <__do_global_dtors_aux>:
  4011e0:	f3 0f 1e fa          	endbr64 
  4011e4:	80 3d ad 2f 00 00 00 	cmp    BYTE PTR [rip+0x2fad],0x0        # 404198 <completed.0>
  4011eb:	75 13                	jne    401200 <__do_global_dtors_aux+0x20>
  4011ed:	55                   	push   rbp
  4011ee:	48 89 e5             	mov    rbp,rsp
  4011f1:	e8 7a ff ff ff       	call   401170 <deregister_tm_clones>
  4011f6:	c6 05 9b 2f 00 00 01 	mov    BYTE PTR [rip+0x2f9b],0x1        # 404198 <completed.0>
  4011fd:	5d                   	pop    rbp
  4011fe:	c3                   	ret    
  4011ff:	90                   	nop
  401200:	c3                   	ret    
  401201:	66 66 2e 0f 1f 84 00 	data16 cs nop WORD PTR [rax+rax*1+0x0]
  401208:	00 00 00 00 
  40120c:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]

0000000000401210 <frame_dummy>:
  401210:	f3 0f 1e fa          	endbr64 
  401214:	eb 8a                	jmp    4011a0 <register_tm_clones>

0000000000401216 <apply_seccomp>:
  401216:	f3 0f 1e fa          	endbr64 
  40121a:	55                   	push   rbp
  40121b:	48 89 e5             	mov    rbp,rsp
  40121e:	41 b8 00 00 00 00    	mov    r8d,0x0
  401224:	b9 00 00 00 00       	mov    ecx,0x0
  401229:	ba 00 00 00 00       	mov    edx,0x0
  40122e:	be 01 00 00 00       	mov    esi,0x1
  401233:	bf 26 00 00 00       	mov    edi,0x26
  401238:	b8 00 00 00 00       	mov    eax,0x0
  40123d:	e8 9e fe ff ff       	call   4010e0 <prctl@plt>
  401242:	85 c0                	test   eax,eax
  401244:	74 19                	je     40125f <apply_seccomp+0x49>
  401246:	48 8d 05 b7 0d 00 00 	lea    rax,[rip+0xdb7]        # 402004 <_IO_stdin_used+0x4>
  40124d:	48 89 c7             	mov    rdi,rax
  401250:	e8 ab fe ff ff       	call   401100 <perror@plt>
  401255:	bf 01 00 00 00       	mov    edi,0x1
  40125a:	e8 c1 fe ff ff       	call   401120 <exit@plt>
  40125f:	48 8d 05 0a 2f 00 00 	lea    rax,[rip+0x2f0a]        # 404170 <filterprog>
  401266:	48 89 c2             	mov    rdx,rax
  401269:	be 02 00 00 00       	mov    esi,0x2
  40126e:	bf 16 00 00 00       	mov    edi,0x16
  401273:	b8 00 00 00 00       	mov    eax,0x0
  401278:	e8 63 fe ff ff       	call   4010e0 <prctl@plt>
  40127d:	83 f8 ff             	cmp    eax,0xffffffff
  401280:	75 19                	jne    40129b <apply_seccomp+0x85>
  401282:	48 8d 05 7b 0d 00 00 	lea    rax,[rip+0xd7b]        # 402004 <_IO_stdin_used+0x4>
  401289:	48 89 c7             	mov    rdi,rax
  40128c:	e8 6f fe ff ff       	call   401100 <perror@plt>
  401291:	bf 01 00 00 00       	mov    edi,0x1
  401296:	e8 85 fe ff ff       	call   401120 <exit@plt>
  40129b:	90                   	nop
  40129c:	5d                   	pop    rbp
  40129d:	c3                   	ret    

000000000040129e <jackpot>:
  40129e:	f3 0f 1e fa          	endbr64 
  4012a2:	55                   	push   rbp
  4012a3:	48 89 e5             	mov    rbp,rsp
  4012a6:	48 8d 05 65 0d 00 00 	lea    rax,[rip+0xd65]        # 402012 <_IO_stdin_used+0x12>
  4012ad:	48 89 c7             	mov    rdi,rax
  4012b0:	e8 fb fd ff ff       	call   4010b0 <puts@plt>
  4012b5:	48 8d 05 68 0d 00 00 	lea    rax,[rip+0xd68]        # 402024 <_IO_stdin_used+0x24>
  4012bc:	48 89 c7             	mov    rdi,rax
  4012bf:	e8 ec fd ff ff       	call   4010b0 <puts@plt>
  4012c4:	90                   	nop
  4012c5:	5d                   	pop    rbp
  4012c6:	c3                   	ret    

00000000004012c7 <main>:
  4012c7:	f3 0f 1e fa          	endbr64 
  4012cb:	55                   	push   rbp
  4012cc:	48 89 e5             	mov    rbp,rsp
  4012cf:	48 81 ec 00 01 00 00 	sub    rsp,0x100
  4012d6:	48 8b 05 b3 2e 00 00 	mov    rax,QWORD PTR [rip+0x2eb3]        # 404190 <stdin@GLIBC_2.2.5>
  4012dd:	b9 00 00 00 00       	mov    ecx,0x0
  4012e2:	ba 02 00 00 00       	mov    edx,0x2
  4012e7:	be 00 00 00 00       	mov    esi,0x0
  4012ec:	48 89 c7             	mov    rdi,rax
  4012ef:	e8 fc fd ff ff       	call   4010f0 <setvbuf@plt>
  4012f4:	48 8b 05 85 2e 00 00 	mov    rax,QWORD PTR [rip+0x2e85]        # 404180 <stdout@GLIBC_2.2.5>
  4012fb:	b9 00 00 00 00       	mov    ecx,0x0
  401300:	ba 02 00 00 00       	mov    edx,0x2
  401305:	be 00 00 00 00       	mov    esi,0x0
  40130a:	48 89 c7             	mov    rdi,rax
  40130d:	e8 de fd ff ff       	call   4010f0 <setvbuf@plt>
  401312:	b8 00 00 00 00       	mov    eax,0x0
  401317:	e8 fa fe ff ff       	call   401216 <apply_seccomp>
  40131c:	48 8b 05 6d 2e 00 00 	mov    rax,QWORD PTR [rip+0x2e6d]        # 404190 <stdin@GLIBC_2.2.5>
  401323:	b9 00 00 00 00       	mov    ecx,0x0
  401328:	ba 02 00 00 00       	mov    edx,0x2
  40132d:	be 00 00 00 00       	mov    esi,0x0
  401332:	48 89 c7             	mov    rdi,rax
  401335:	e8 b6 fd ff ff       	call   4010f0 <setvbuf@plt>
  40133a:	48 8b 05 3f 2e 00 00 	mov    rax,QWORD PTR [rip+0x2e3f]        # 404180 <stdout@GLIBC_2.2.5>
  401341:	b9 00 00 00 00       	mov    ecx,0x0
  401346:	ba 02 00 00 00       	mov    edx,0x2
  40134b:	be 00 00 00 00       	mov    esi,0x0
  401350:	48 89 c7             	mov    rdi,rax
  401353:	e8 98 fd ff ff       	call   4010f0 <setvbuf@plt>
  401358:	48 8d 05 d0 0c 00 00 	lea    rax,[rip+0xcd0]        # 40202f <_IO_stdin_used+0x2f>
  40135f:	48 89 c7             	mov    rdi,rax
  401362:	e8 49 fd ff ff       	call   4010b0 <puts@plt>
  401367:	48 8d 05 cb 0c 00 00 	lea    rax,[rip+0xccb]        # 402039 <_IO_stdin_used+0x39>
  40136e:	48 89 c7             	mov    rdi,rax
  401371:	b8 00 00 00 00       	mov    eax,0x0
  401376:	e8 45 fd ff ff       	call   4010c0 <printf@plt>
  40137b:	48 8d 85 0c ff ff ff 	lea    rax,[rbp-0xf4]
  401382:	48 89 c6             	mov    rsi,rax
  401385:	48 8d 05 c3 0c 00 00 	lea    rax,[rip+0xcc3]        # 40204f <_IO_stdin_used+0x4f>
  40138c:	48 89 c7             	mov    rdi,rax
  40138f:	b8 00 00 00 00       	mov    eax,0x0
  401394:	e8 77 fd ff ff       	call   401110 <__isoc99_scanf@plt>
  401399:	8b 85 0c ff ff ff    	mov    eax,DWORD PTR [rbp-0xf4]
  40139f:	48 98                	cdqe   
  4013a1:	48 8b 84 c5 10 ff ff 	mov    rax,QWORD PTR [rbp+rax*8-0xf0]
  4013a8:	ff 
  4013a9:	48 89 c6             	mov    rsi,rax
  4013ac:	48 8d 05 9f 0c 00 00 	lea    rax,[rip+0xc9f]        # 402052 <_IO_stdin_used+0x52>
  4013b3:	48 89 c7             	mov    rdi,rax
  4013b6:	b8 00 00 00 00       	mov    eax,0x0
  4013bb:	e8 00 fd ff ff       	call   4010c0 <printf@plt>
  4013c0:	48 8d 05 a6 0c 00 00 	lea    rax,[rip+0xca6]        # 40206d <_IO_stdin_used+0x6d>
  4013c7:	48 89 c7             	mov    rdi,rax
  4013ca:	b8 00 00 00 00       	mov    eax,0x0
  4013cf:	e8 ec fc ff ff       	call   4010c0 <printf@plt>
  4013d4:	48 8d 45 90          	lea    rax,[rbp-0x70]
  4013d8:	ba 00 01 00 00       	mov    edx,0x100
  4013dd:	48 89 c6             	mov    rsi,rax
  4013e0:	bf 00 00 00 00       	mov    edi,0x0
  4013e5:	e8 e6 fc ff ff       	call   4010d0 <read@plt>
  4013ea:	8b 85 0c ff ff ff    	mov    eax,DWORD PTR [rbp-0xf4]
  4013f0:	48 98                	cdqe   
  4013f2:	48 8b 84 c5 10 ff ff 	mov    rax,QWORD PTR [rbp+rax*8-0xf0]
  4013f9:	ff 
  4013fa:	48 89 c2             	mov    rdx,rax
  4013fd:	48 8d 05 9a fe ff ff 	lea    rax,[rip+0xfffffffffffffe9a]        # 40129e <jackpot>
  401404:	48 39 c2             	cmp    rdx,rax
  401407:	75 1b                	jne    401424 <main+0x15d>
  401409:	48 8d 05 6e 0c 00 00 	lea    rax,[rip+0xc6e]        # 40207e <_IO_stdin_used+0x7e>
  401410:	48 89 c7             	mov    rdi,rax
  401413:	e8 98 fc ff ff       	call   4010b0 <puts@plt>
  401418:	b8 00 00 00 00       	mov    eax,0x0
  40141d:	e8 7c fe ff ff       	call   40129e <jackpot>
  401422:	eb 0f                	jmp    401433 <main+0x16c>
  401424:	48 8d 05 69 0c 00 00 	lea    rax,[rip+0xc69]        # 402094 <_IO_stdin_used+0x94>
  40142b:	48 89 c7             	mov    rdi,rax
  40142e:	e8 7d fc ff ff       	call   4010b0 <puts@plt>
  401433:	b8 00 00 00 00       	mov    eax,0x0
  401438:	c9                   	leave  
  401439:	c3                   	ret    

Disassembly of section .fini:

000000000040143c <_fini>:
  40143c:	f3 0f 1e fa          	endbr64 
  401440:	48 83 ec 08          	sub    rsp,0x8
  401444:	48 83 c4 08          	add    rsp,0x8
  401448:	c3                   	ret    
