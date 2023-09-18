
easy-c2:     file format elf64-x86-64


Disassembly of section .init:

0000000000001000 <_init>:
    1000:	f3 0f 1e fa          	endbr64 
    1004:	48 83 ec 08          	sub    $0x8,%rsp
    1008:	48 8b 05 d9 2f 00 00 	mov    0x2fd9(%rip),%rax        # 3fe8 <__gmon_start__>
    100f:	48 85 c0             	test   %rax,%rax
    1012:	74 02                	je     1016 <_init+0x16>
    1014:	ff d0                	call   *%rax
    1016:	48 83 c4 08          	add    $0x8,%rsp
    101a:	c3                   	ret    

Disassembly of section .plt:

0000000000001020 <.plt>:
    1020:	ff 35 2a 2f 00 00    	push   0x2f2a(%rip)        # 3f50 <_GLOBAL_OFFSET_TABLE_+0x8>
    1026:	f2 ff 25 2b 2f 00 00 	bnd jmp *0x2f2b(%rip)        # 3f58 <_GLOBAL_OFFSET_TABLE_+0x10>
    102d:	0f 1f 00             	nopl   (%rax)
    1030:	f3 0f 1e fa          	endbr64 
    1034:	68 00 00 00 00       	push   $0x0
    1039:	f2 e9 e1 ff ff ff    	bnd jmp 1020 <.plt>
    103f:	90                   	nop
    1040:	f3 0f 1e fa          	endbr64 
    1044:	68 01 00 00 00       	push   $0x1
    1049:	f2 e9 d1 ff ff ff    	bnd jmp 1020 <.plt>
    104f:	90                   	nop
    1050:	f3 0f 1e fa          	endbr64 
    1054:	68 02 00 00 00       	push   $0x2
    1059:	f2 e9 c1 ff ff ff    	bnd jmp 1020 <.plt>
    105f:	90                   	nop
    1060:	f3 0f 1e fa          	endbr64 
    1064:	68 03 00 00 00       	push   $0x3
    1069:	f2 e9 b1 ff ff ff    	bnd jmp 1020 <.plt>
    106f:	90                   	nop
    1070:	f3 0f 1e fa          	endbr64 
    1074:	68 04 00 00 00       	push   $0x4
    1079:	f2 e9 a1 ff ff ff    	bnd jmp 1020 <.plt>
    107f:	90                   	nop
    1080:	f3 0f 1e fa          	endbr64 
    1084:	68 05 00 00 00       	push   $0x5
    1089:	f2 e9 91 ff ff ff    	bnd jmp 1020 <.plt>
    108f:	90                   	nop
    1090:	f3 0f 1e fa          	endbr64 
    1094:	68 06 00 00 00       	push   $0x6
    1099:	f2 e9 81 ff ff ff    	bnd jmp 1020 <.plt>
    109f:	90                   	nop
    10a0:	f3 0f 1e fa          	endbr64 
    10a4:	68 07 00 00 00       	push   $0x7
    10a9:	f2 e9 71 ff ff ff    	bnd jmp 1020 <.plt>
    10af:	90                   	nop
    10b0:	f3 0f 1e fa          	endbr64 
    10b4:	68 08 00 00 00       	push   $0x8
    10b9:	f2 e9 61 ff ff ff    	bnd jmp 1020 <.plt>
    10bf:	90                   	nop
    10c0:	f3 0f 1e fa          	endbr64 
    10c4:	68 09 00 00 00       	push   $0x9
    10c9:	f2 e9 51 ff ff ff    	bnd jmp 1020 <.plt>
    10cf:	90                   	nop
    10d0:	f3 0f 1e fa          	endbr64 
    10d4:	68 0a 00 00 00       	push   $0xa
    10d9:	f2 e9 41 ff ff ff    	bnd jmp 1020 <.plt>
    10df:	90                   	nop
    10e0:	f3 0f 1e fa          	endbr64 
    10e4:	68 0b 00 00 00       	push   $0xb
    10e9:	f2 e9 31 ff ff ff    	bnd jmp 1020 <.plt>
    10ef:	90                   	nop
    10f0:	f3 0f 1e fa          	endbr64 
    10f4:	68 0c 00 00 00       	push   $0xc
    10f9:	f2 e9 21 ff ff ff    	bnd jmp 1020 <.plt>
    10ff:	90                   	nop
    1100:	f3 0f 1e fa          	endbr64 
    1104:	68 0d 00 00 00       	push   $0xd
    1109:	f2 e9 11 ff ff ff    	bnd jmp 1020 <.plt>
    110f:	90                   	nop
    1110:	f3 0f 1e fa          	endbr64 
    1114:	68 0e 00 00 00       	push   $0xe
    1119:	f2 e9 01 ff ff ff    	bnd jmp 1020 <.plt>
    111f:	90                   	nop

Disassembly of section .plt.got:

0000000000001120 <__cxa_finalize@plt>:
    1120:	f3 0f 1e fa          	endbr64 
    1124:	f2 ff 25 cd 2e 00 00 	bnd jmp *0x2ecd(%rip)        # 3ff8 <__cxa_finalize@GLIBC_2.2.5>
    112b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

Disassembly of section .plt.sec:

0000000000001130 <free@plt>:
    1130:	f3 0f 1e fa          	endbr64 
    1134:	f2 ff 25 25 2e 00 00 	bnd jmp *0x2e25(%rip)        # 3f60 <free@GLIBC_2.2.5>
    113b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

0000000000001140 <puts@plt>:
    1140:	f3 0f 1e fa          	endbr64 
    1144:	f2 ff 25 1d 2e 00 00 	bnd jmp *0x2e1d(%rip)        # 3f68 <puts@GLIBC_2.2.5>
    114b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

0000000000001150 <write@plt>:
    1150:	f3 0f 1e fa          	endbr64 
    1154:	f2 ff 25 15 2e 00 00 	bnd jmp *0x2e15(%rip)        # 3f70 <write@GLIBC_2.2.5>
    115b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

0000000000001160 <strlen@plt>:
    1160:	f3 0f 1e fa          	endbr64 
    1164:	f2 ff 25 0d 2e 00 00 	bnd jmp *0x2e0d(%rip)        # 3f78 <strlen@GLIBC_2.2.5>
    116b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

0000000000001170 <__stack_chk_fail@plt>:
    1170:	f3 0f 1e fa          	endbr64 
    1174:	f2 ff 25 05 2e 00 00 	bnd jmp *0x2e05(%rip)        # 3f80 <__stack_chk_fail@GLIBC_2.4>
    117b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

0000000000001180 <htons@plt>:
    1180:	f3 0f 1e fa          	endbr64 
    1184:	f2 ff 25 fd 2d 00 00 	bnd jmp *0x2dfd(%rip)        # 3f88 <htons@GLIBC_2.2.5>
    118b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

0000000000001190 <close@plt>:
    1190:	f3 0f 1e fa          	endbr64 
    1194:	f2 ff 25 f5 2d 00 00 	bnd jmp *0x2df5(%rip)        # 3f90 <close@GLIBC_2.2.5>
    119b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

00000000000011a0 <inet_addr@plt>:
    11a0:	f3 0f 1e fa          	endbr64 
    11a4:	f2 ff 25 ed 2d 00 00 	bnd jmp *0x2ded(%rip)        # 3f98 <inet_addr@GLIBC_2.2.5>
    11ab:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

00000000000011b0 <malloc@plt>:
    11b0:	f3 0f 1e fa          	endbr64 
    11b4:	f2 ff 25 e5 2d 00 00 	bnd jmp *0x2de5(%rip)        # 3fa0 <malloc@GLIBC_2.2.5>
    11bb:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

00000000000011c0 <perror@plt>:
    11c0:	f3 0f 1e fa          	endbr64 
    11c4:	f2 ff 25 dd 2d 00 00 	bnd jmp *0x2ddd(%rip)        # 3fa8 <perror@GLIBC_2.2.5>
    11cb:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

00000000000011d0 <sprintf@plt>:
    11d0:	f3 0f 1e fa          	endbr64 
    11d4:	f2 ff 25 d5 2d 00 00 	bnd jmp *0x2dd5(%rip)        # 3fb0 <sprintf@GLIBC_2.2.5>
    11db:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

00000000000011e0 <exit@plt>:
    11e0:	f3 0f 1e fa          	endbr64 
    11e4:	f2 ff 25 cd 2d 00 00 	bnd jmp *0x2dcd(%rip)        # 3fb8 <exit@GLIBC_2.2.5>
    11eb:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

00000000000011f0 <connect@plt>:
    11f0:	f3 0f 1e fa          	endbr64 
    11f4:	f2 ff 25 c5 2d 00 00 	bnd jmp *0x2dc5(%rip)        # 3fc0 <connect@GLIBC_2.2.5>
    11fb:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

0000000000001200 <sleep@plt>:
    1200:	f3 0f 1e fa          	endbr64 
    1204:	f2 ff 25 bd 2d 00 00 	bnd jmp *0x2dbd(%rip)        # 3fc8 <sleep@GLIBC_2.2.5>
    120b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

0000000000001210 <socket@plt>:
    1210:	f3 0f 1e fa          	endbr64 
    1214:	f2 ff 25 b5 2d 00 00 	bnd jmp *0x2db5(%rip)        # 3fd0 <socket@GLIBC_2.2.5>
    121b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

Disassembly of section .text:

0000000000001220 <_start>:
    1220:	f3 0f 1e fa          	endbr64 
    1224:	31 ed                	xor    %ebp,%ebp
    1226:	49 89 d1             	mov    %rdx,%r9
    1229:	5e                   	pop    %rsi
    122a:	48 89 e2             	mov    %rsp,%rdx
    122d:	48 83 e4 f0          	and    $0xfffffffffffffff0,%rsp
    1231:	50                   	push   %rax
    1232:	54                   	push   %rsp
    1233:	4c 8d 05 e6 04 00 00 	lea    0x4e6(%rip),%r8        # 1720 <__libc_csu_fini>
    123a:	48 8d 0d 6f 04 00 00 	lea    0x46f(%rip),%rcx        # 16b0 <__libc_csu_init>
    1241:	48 8d 3d 9f 03 00 00 	lea    0x39f(%rip),%rdi        # 15e7 <main>
    1248:	ff 15 92 2d 00 00    	call   *0x2d92(%rip)        # 3fe0 <__libc_start_main@GLIBC_2.2.5>
    124e:	f4                   	hlt    
    124f:	90                   	nop

0000000000001250 <deregister_tm_clones>:
    1250:	48 8d 3d b9 2d 00 00 	lea    0x2db9(%rip),%rdi        # 4010 <__TMC_END__>
    1257:	48 8d 05 b2 2d 00 00 	lea    0x2db2(%rip),%rax        # 4010 <__TMC_END__>
    125e:	48 39 f8             	cmp    %rdi,%rax
    1261:	74 15                	je     1278 <deregister_tm_clones+0x28>
    1263:	48 8b 05 6e 2d 00 00 	mov    0x2d6e(%rip),%rax        # 3fd8 <_ITM_deregisterTMCloneTable>
    126a:	48 85 c0             	test   %rax,%rax
    126d:	74 09                	je     1278 <deregister_tm_clones+0x28>
    126f:	ff e0                	jmp    *%rax
    1271:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
    1278:	c3                   	ret    
    1279:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)

0000000000001280 <register_tm_clones>:
    1280:	48 8d 3d 89 2d 00 00 	lea    0x2d89(%rip),%rdi        # 4010 <__TMC_END__>
    1287:	48 8d 35 82 2d 00 00 	lea    0x2d82(%rip),%rsi        # 4010 <__TMC_END__>
    128e:	48 29 fe             	sub    %rdi,%rsi
    1291:	48 89 f0             	mov    %rsi,%rax
    1294:	48 c1 ee 3f          	shr    $0x3f,%rsi
    1298:	48 c1 f8 03          	sar    $0x3,%rax
    129c:	48 01 c6             	add    %rax,%rsi
    129f:	48 d1 fe             	sar    %rsi
    12a2:	74 14                	je     12b8 <register_tm_clones+0x38>
    12a4:	48 8b 05 45 2d 00 00 	mov    0x2d45(%rip),%rax        # 3ff0 <_ITM_registerTMCloneTable>
    12ab:	48 85 c0             	test   %rax,%rax
    12ae:	74 08                	je     12b8 <register_tm_clones+0x38>
    12b0:	ff e0                	jmp    *%rax
    12b2:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
    12b8:	c3                   	ret    
    12b9:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)

00000000000012c0 <__do_global_dtors_aux>:
    12c0:	f3 0f 1e fa          	endbr64 
    12c4:	80 3d 45 2d 00 00 00 	cmpb   $0x0,0x2d45(%rip)        # 4010 <__TMC_END__>
    12cb:	75 2b                	jne    12f8 <__do_global_dtors_aux+0x38>
    12cd:	55                   	push   %rbp
    12ce:	48 83 3d 22 2d 00 00 	cmpq   $0x0,0x2d22(%rip)        # 3ff8 <__cxa_finalize@GLIBC_2.2.5>
    12d5:	00 
    12d6:	48 89 e5             	mov    %rsp,%rbp
    12d9:	74 0c                	je     12e7 <__do_global_dtors_aux+0x27>
    12db:	48 8b 3d 26 2d 00 00 	mov    0x2d26(%rip),%rdi        # 4008 <__dso_handle>
    12e2:	e8 39 fe ff ff       	call   1120 <__cxa_finalize@plt>
    12e7:	e8 64 ff ff ff       	call   1250 <deregister_tm_clones>
    12ec:	c6 05 1d 2d 00 00 01 	movb   $0x1,0x2d1d(%rip)        # 4010 <__TMC_END__>
    12f3:	5d                   	pop    %rbp
    12f4:	c3                   	ret    
    12f5:	0f 1f 00             	nopl   (%rax)
    12f8:	c3                   	ret    
    12f9:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)

0000000000001300 <frame_dummy>:
    1300:	f3 0f 1e fa          	endbr64 
    1304:	e9 77 ff ff ff       	jmp    1280 <register_tm_clones>

0000000000001309 <err>:
    1309:	f3 0f 1e fa          	endbr64 
    130d:	55                   	push   %rbp
    130e:	48 89 e5             	mov    %rsp,%rbp
    1311:	48 83 ec 10          	sub    $0x10,%rsp
    1315:	48 89 7d f8          	mov    %rdi,-0x8(%rbp)
    1319:	48 8b 45 f8          	mov    -0x8(%rbp),%rax
    131d:	48 89 c7             	mov    %rax,%rdi
    1320:	e8 9b fe ff ff       	call   11c0 <perror@plt>
    1325:	bf 00 00 00 00       	mov    $0x0,%edi
    132a:	e8 b1 fe ff ff       	call   11e0 <exit@plt>

000000000000132f <socket_connect>:
    132f:	f3 0f 1e fa          	endbr64 
    1333:	55                   	push   %rbp
    1334:	48 89 e5             	mov    %rsp,%rbp
    1337:	48 83 ec 40          	sub    $0x40,%rsp
    133b:	48 89 7d c8          	mov    %rdi,-0x38(%rbp)
    133f:	89 75 c4             	mov    %esi,-0x3c(%rbp)
    1342:	64 48 8b 04 25 28 00 	mov    %fs:0x28,%rax
    1349:	00 00 
    134b:	48 89 45 f8          	mov    %rax,-0x8(%rbp)
    134f:	31 c0                	xor    %eax,%eax
    1351:	ba 00 00 00 00       	mov    $0x0,%edx
    1356:	be 01 00 00 00       	mov    $0x1,%esi
    135b:	bf 02 00 00 00       	mov    $0x2,%edi
    1360:	e8 ab fe ff ff       	call   1210 <socket@plt>
    1365:	89 45 dc             	mov    %eax,-0x24(%rbp)
    1368:	83 7d dc ff          	cmpl   $0xffffffff,-0x24(%rbp)
    136c:	75 0c                	jne    137a <socket_connect+0x4b>
    136e:	48 8d 3d 93 0c 00 00 	lea    0xc93(%rip),%rdi        # 2008 <_IO_stdin_used+0x8>
    1375:	e8 8f ff ff ff       	call   1309 <err>
    137a:	66 c7 45 e0 02 00    	movw   $0x2,-0x20(%rbp)
    1380:	8b 45 c4             	mov    -0x3c(%rbp),%eax
    1383:	0f b7 c0             	movzwl %ax,%eax
    1386:	89 c7                	mov    %eax,%edi
    1388:	e8 f3 fd ff ff       	call   1180 <htons@plt>
    138d:	66 89 45 e2          	mov    %ax,-0x1e(%rbp)
    1391:	48 8b 45 c8          	mov    -0x38(%rbp),%rax
    1395:	48 89 c7             	mov    %rax,%rdi
    1398:	e8 03 fe ff ff       	call   11a0 <inet_addr@plt>
    139d:	89 45 e4             	mov    %eax,-0x1c(%rbp)
    13a0:	48 8d 4d e0          	lea    -0x20(%rbp),%rcx
    13a4:	8b 45 dc             	mov    -0x24(%rbp),%eax
    13a7:	ba 10 00 00 00       	mov    $0x10,%edx
    13ac:	48 89 ce             	mov    %rcx,%rsi
    13af:	89 c7                	mov    %eax,%edi
    13b1:	e8 3a fe ff ff       	call   11f0 <connect@plt>
    13b6:	83 f8 ff             	cmp    $0xffffffff,%eax
    13b9:	75 0c                	jne    13c7 <socket_connect+0x98>
    13bb:	48 8d 3d 62 0c 00 00 	lea    0xc62(%rip),%rdi        # 2024 <_IO_stdin_used+0x24>
    13c2:	e8 42 ff ff ff       	call   1309 <err>
    13c7:	8b 45 dc             	mov    -0x24(%rbp),%eax
    13ca:	48 8b 55 f8          	mov    -0x8(%rbp),%rdx
    13ce:	64 48 33 14 25 28 00 	xor    %fs:0x28,%rdx
    13d5:	00 00 
    13d7:	74 05                	je     13de <socket_connect+0xaf>
    13d9:	e8 92 fd ff ff       	call   1170 <__stack_chk_fail@plt>
    13de:	c9                   	leave  
    13df:	c3                   	ret    

00000000000013e0 <send_msg>:
    13e0:	f3 0f 1e fa          	endbr64 
    13e4:	55                   	push   %rbp
    13e5:	48 89 e5             	mov    %rsp,%rbp
    13e8:	48 81 ec 40 04 00 00 	sub    $0x440,%rsp
    13ef:	89 bd cc fb ff ff    	mov    %edi,-0x434(%rbp)
    13f5:	48 89 b5 c0 fb ff ff 	mov    %rsi,-0x440(%rbp)
    13fc:	64 48 8b 04 25 28 00 	mov    %fs:0x28,%rax
    1403:	00 00 
    1405:	48 89 45 f8          	mov    %rax,-0x8(%rbp)
    1409:	31 c0                	xor    %eax,%eax
    140b:	48 8d 05 36 0c 00 00 	lea    0xc36(%rip),%rax        # 2048 <_IO_stdin_used+0x48>
    1412:	48 89 85 e8 fb ff ff 	mov    %rax,-0x418(%rbp)
    1419:	48 8b 95 c0 fb ff ff 	mov    -0x440(%rbp),%rdx
    1420:	48 8b 8d e8 fb ff ff 	mov    -0x418(%rbp),%rcx
    1427:	48 8d 85 f0 fb ff ff 	lea    -0x410(%rbp),%rax
    142e:	48 89 ce             	mov    %rcx,%rsi
    1431:	48 89 c7             	mov    %rax,%rdi
    1434:	b8 00 00 00 00       	mov    $0x0,%eax
    1439:	e8 92 fd ff ff       	call   11d0 <sprintf@plt>
    143e:	48 8d 85 f0 fb ff ff 	lea    -0x410(%rbp),%rax
    1445:	48 89 c7             	mov    %rax,%rdi
    1448:	e8 13 fd ff ff       	call   1160 <strlen@plt>
    144d:	89 85 e0 fb ff ff    	mov    %eax,-0x420(%rbp)
    1453:	c7 85 dc fb ff ff 00 	movl   $0x0,-0x424(%rbp)
    145a:	00 00 00 
    145d:	8b 85 e0 fb ff ff    	mov    -0x420(%rbp),%eax
    1463:	2b 85 dc fb ff ff    	sub    -0x424(%rbp),%eax
    1469:	48 63 d0             	movslq %eax,%rdx
    146c:	8b 85 dc fb ff ff    	mov    -0x424(%rbp),%eax
    1472:	48 98                	cltq   
    1474:	48 8d 8d f0 fb ff ff 	lea    -0x410(%rbp),%rcx
    147b:	48 01 c1             	add    %rax,%rcx
    147e:	8b 85 cc fb ff ff    	mov    -0x434(%rbp),%eax
    1484:	48 89 ce             	mov    %rcx,%rsi
    1487:	89 c7                	mov    %eax,%edi
    1489:	e8 c2 fc ff ff       	call   1150 <write@plt>
    148e:	89 85 e4 fb ff ff    	mov    %eax,-0x41c(%rbp)
    1494:	83 bd e4 fb ff ff ff 	cmpl   $0xffffffff,-0x41c(%rbp)
    149b:	75 0c                	jne    14a9 <send_msg+0xc9>
    149d:	48 8d 3d 32 0c 00 00 	lea    0xc32(%rip),%rdi        # 20d6 <_IO_stdin_used+0xd6>
    14a4:	e8 60 fe ff ff       	call   1309 <err>
    14a9:	83 bd e4 fb ff ff 00 	cmpl   $0x0,-0x41c(%rbp)
    14b0:	74 1c                	je     14ce <send_msg+0xee>
    14b2:	8b 85 e4 fb ff ff    	mov    -0x41c(%rbp),%eax
    14b8:	01 85 dc fb ff ff    	add    %eax,-0x424(%rbp)
    14be:	8b 85 dc fb ff ff    	mov    -0x424(%rbp),%eax
    14c4:	3b 85 e0 fb ff ff    	cmp    -0x420(%rbp),%eax
    14ca:	7c 91                	jl     145d <send_msg+0x7d>
    14cc:	eb 01                	jmp    14cf <send_msg+0xef>
    14ce:	90                   	nop
    14cf:	90                   	nop
    14d0:	48 8b 45 f8          	mov    -0x8(%rbp),%rax
    14d4:	64 48 33 04 25 28 00 	xor    %fs:0x28,%rax
    14db:	00 00 
    14dd:	74 05                	je     14e4 <send_msg+0x104>
    14df:	e8 8c fc ff ff       	call   1170 <__stack_chk_fail@plt>
    14e4:	c9                   	leave  
    14e5:	c3                   	ret    

00000000000014e6 <decode_flag>:
    14e6:	f3 0f 1e fa          	endbr64 
    14ea:	55                   	push   %rbp
    14eb:	48 89 e5             	mov    %rsp,%rbp
    14ee:	48 83 ec 20          	sub    $0x20,%rsp
    14f2:	48 89 7d e8          	mov    %rdi,-0x18(%rbp)
    14f6:	48 89 75 e0          	mov    %rsi,-0x20(%rbp)
    14fa:	48 8b 45 e0          	mov    -0x20(%rbp),%rax
    14fe:	48 89 c7             	mov    %rax,%rdi
    1501:	e8 5a fc ff ff       	call   1160 <strlen@plt>
    1506:	89 45 f8             	mov    %eax,-0x8(%rbp)
    1509:	8b 45 f8             	mov    -0x8(%rbp),%eax
    150c:	89 c2                	mov    %eax,%edx
    150e:	c1 ea 1f             	shr    $0x1f,%edx
    1511:	01 d0                	add    %edx,%eax
    1513:	d1 f8                	sar    %eax
    1515:	83 c0 01             	add    $0x1,%eax
    1518:	48 98                	cltq   
    151a:	48 89 c7             	mov    %rax,%rdi
    151d:	e8 8e fc ff ff       	call   11b0 <malloc@plt>
    1522:	48 89 c2             	mov    %rax,%rdx
    1525:	48 8b 45 e8          	mov    -0x18(%rbp),%rax
    1529:	48 89 10             	mov    %rdx,(%rax)
    152c:	c7 45 f4 00 00 00 00 	movl   $0x0,-0xc(%rbp)
    1533:	e9 9f 00 00 00       	jmp    15d7 <decode_flag+0xf1>
    1538:	8b 45 f4             	mov    -0xc(%rbp),%eax
    153b:	48 63 d0             	movslq %eax,%rdx
    153e:	48 8b 45 e0          	mov    -0x20(%rbp),%rax
    1542:	48 01 d0             	add    %rdx,%rax
    1545:	0f b7 00             	movzwl (%rax),%eax
    1548:	66 89 45 f2          	mov    %ax,-0xe(%rbp)
    154c:	0f b7 45 f2          	movzwl -0xe(%rbp),%eax
    1550:	89 45 fc             	mov    %eax,-0x4(%rbp)
    1553:	8b 45 fc             	mov    -0x4(%rbp),%eax
    1556:	05 8b 04 00 00       	add    $0x48b,%eax
    155b:	48 63 d0             	movslq %eax,%rdx
    155e:	48 69 d2 b7 49 6c 3a 	imul   $0x3a6c49b7,%rdx,%rdx
    1565:	48 c1 ea 20          	shr    $0x20,%rdx
    1569:	89 d1                	mov    %edx,%ecx
    156b:	c1 f9 0a             	sar    $0xa,%ecx
    156e:	99                   	cltd   
    156f:	29 d1                	sub    %edx,%ecx
    1571:	89 ca                	mov    %ecx,%edx
    1573:	89 55 fc             	mov    %edx,-0x4(%rbp)
    1576:	8b 55 fc             	mov    -0x4(%rbp),%edx
    1579:	69 d2 87 11 00 00    	imul   $0x1187,%edx,%edx
    157f:	29 d0                	sub    %edx,%eax
    1581:	89 45 fc             	mov    %eax,-0x4(%rbp)
    1584:	8b 45 fc             	mov    -0x4(%rbp),%eax
    1587:	69 c0 e7 04 00 00    	imul   $0x4e7,%eax,%eax
    158d:	48 63 d0             	movslq %eax,%rdx
    1590:	48 69 d2 b7 49 6c 3a 	imul   $0x3a6c49b7,%rdx,%rdx
    1597:	48 c1 ea 20          	shr    $0x20,%rdx
    159b:	89 d1                	mov    %edx,%ecx
    159d:	c1 f9 0a             	sar    $0xa,%ecx
    15a0:	99                   	cltd   
    15a1:	29 d1                	sub    %edx,%ecx
    15a3:	89 ca                	mov    %ecx,%edx
    15a5:	89 55 fc             	mov    %edx,-0x4(%rbp)
    15a8:	8b 55 fc             	mov    -0x4(%rbp),%edx
    15ab:	69 d2 87 11 00 00    	imul   $0x1187,%edx,%edx
    15b1:	29 d0                	sub    %edx,%eax
    15b3:	89 45 fc             	mov    %eax,-0x4(%rbp)
    15b6:	48 8b 45 e8          	mov    -0x18(%rbp),%rax
    15ba:	48 8b 10             	mov    (%rax),%rdx
    15bd:	8b 45 f4             	mov    -0xc(%rbp),%eax
    15c0:	89 c1                	mov    %eax,%ecx
    15c2:	c1 e9 1f             	shr    $0x1f,%ecx
    15c5:	01 c8                	add    %ecx,%eax
    15c7:	d1 f8                	sar    %eax
    15c9:	48 98                	cltq   
    15cb:	48 01 d0             	add    %rdx,%rax
    15ce:	8b 55 fc             	mov    -0x4(%rbp),%edx
    15d1:	88 10                	mov    %dl,(%rax)
    15d3:	83 45 f4 02          	addl   $0x2,-0xc(%rbp)
    15d7:	8b 45 f4             	mov    -0xc(%rbp),%eax
    15da:	3b 45 f8             	cmp    -0x8(%rbp),%eax
    15dd:	0f 8c 55 ff ff ff    	jl     1538 <decode_flag+0x52>
    15e3:	90                   	nop
    15e4:	90                   	nop
    15e5:	c9                   	leave  
    15e6:	c3                   	ret    

00000000000015e7 <main>:
    15e7:	f3 0f 1e fa          	endbr64 
    15eb:	55                   	push   %rbp
    15ec:	48 89 e5             	mov    %rsp,%rbp
    15ef:	48 83 ec 40          	sub    $0x40,%rsp
    15f3:	89 7d cc             	mov    %edi,-0x34(%rbp)
    15f6:	48 89 75 c0          	mov    %rsi,-0x40(%rbp)
    15fa:	64 48 8b 04 25 28 00 	mov    %fs:0x28,%rax
    1601:	00 00 
    1603:	48 89 45 f8          	mov    %rax,-0x8(%rbp)
    1607:	31 c0                	xor    %eax,%eax
    1609:	48 8d 05 e0 0a 00 00 	lea    0xae0(%rip),%rax        # 20f0 <_IO_stdin_used+0xf0>
    1610:	48 89 45 e8          	mov    %rax,-0x18(%rbp)
    1614:	48 8d 05 0c 0b 00 00 	lea    0xb0c(%rip),%rax        # 2127 <_IO_stdin_used+0x127>
    161b:	48 89 45 f0          	mov    %rax,-0x10(%rbp)
    161f:	c7 45 d8 b3 2b 00 00 	movl   $0x2bb3,-0x28(%rbp)
    1626:	8b 55 d8             	mov    -0x28(%rbp),%edx
    1629:	48 8b 45 f0          	mov    -0x10(%rbp),%rax
    162d:	89 d6                	mov    %edx,%esi
    162f:	48 89 c7             	mov    %rax,%rdi
    1632:	e8 f8 fc ff ff       	call   132f <socket_connect>
    1637:	89 45 dc             	mov    %eax,-0x24(%rbp)
    163a:	48 8b 55 e8          	mov    -0x18(%rbp),%rdx
    163e:	48 8d 45 e0          	lea    -0x20(%rbp),%rax
    1642:	48 89 d6             	mov    %rdx,%rsi
    1645:	48 89 c7             	mov    %rax,%rdi
    1648:	e8 99 fe ff ff       	call   14e6 <decode_flag>
    164d:	48 8b 55 e0          	mov    -0x20(%rbp),%rdx
    1651:	8b 45 dc             	mov    -0x24(%rbp),%eax
    1654:	48 89 d6             	mov    %rdx,%rsi
    1657:	89 c7                	mov    %eax,%edi
    1659:	e8 82 fd ff ff       	call   13e0 <send_msg>
    165e:	48 8d 3d cc 0a 00 00 	lea    0xacc(%rip),%rdi        # 2131 <_IO_stdin_used+0x131>
    1665:	e8 d6 fa ff ff       	call   1140 <puts@plt>
    166a:	bf 01 00 00 00       	mov    $0x1,%edi
    166f:	e8 8c fb ff ff       	call   1200 <sleep@plt>
    1674:	48 8b 45 e0          	mov    -0x20(%rbp),%rax
    1678:	48 89 c7             	mov    %rax,%rdi
    167b:	e8 b0 fa ff ff       	call   1130 <free@plt>
    1680:	8b 45 dc             	mov    -0x24(%rbp),%eax
    1683:	89 c7                	mov    %eax,%edi
    1685:	e8 06 fb ff ff       	call   1190 <close@plt>
    168a:	b8 00 00 00 00       	mov    $0x0,%eax
    168f:	48 8b 4d f8          	mov    -0x8(%rbp),%rcx
    1693:	64 48 33 0c 25 28 00 	xor    %fs:0x28,%rcx
    169a:	00 00 
    169c:	74 05                	je     16a3 <main+0xbc>
    169e:	e8 cd fa ff ff       	call   1170 <__stack_chk_fail@plt>
    16a3:	c9                   	leave  
    16a4:	c3                   	ret    
    16a5:	66 2e 0f 1f 84 00 00 	cs nopw 0x0(%rax,%rax,1)
    16ac:	00 00 00 
    16af:	90                   	nop

00000000000016b0 <__libc_csu_init>:
    16b0:	f3 0f 1e fa          	endbr64 
    16b4:	41 57                	push   %r15
    16b6:	4c 8d 3d 8b 26 00 00 	lea    0x268b(%rip),%r15        # 3d48 <__frame_dummy_init_array_entry>
    16bd:	41 56                	push   %r14
    16bf:	49 89 d6             	mov    %rdx,%r14
    16c2:	41 55                	push   %r13
    16c4:	49 89 f5             	mov    %rsi,%r13
    16c7:	41 54                	push   %r12
    16c9:	41 89 fc             	mov    %edi,%r12d
    16cc:	55                   	push   %rbp
    16cd:	48 8d 2d 7c 26 00 00 	lea    0x267c(%rip),%rbp        # 3d50 <__do_global_dtors_aux_fini_array_entry>
    16d4:	53                   	push   %rbx
    16d5:	4c 29 fd             	sub    %r15,%rbp
    16d8:	48 83 ec 08          	sub    $0x8,%rsp
    16dc:	e8 1f f9 ff ff       	call   1000 <_init>
    16e1:	48 c1 fd 03          	sar    $0x3,%rbp
    16e5:	74 1f                	je     1706 <__libc_csu_init+0x56>
    16e7:	31 db                	xor    %ebx,%ebx
    16e9:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
    16f0:	4c 89 f2             	mov    %r14,%rdx
    16f3:	4c 89 ee             	mov    %r13,%rsi
    16f6:	44 89 e7             	mov    %r12d,%edi
    16f9:	41 ff 14 df          	call   *(%r15,%rbx,8)
    16fd:	48 83 c3 01          	add    $0x1,%rbx
    1701:	48 39 dd             	cmp    %rbx,%rbp
    1704:	75 ea                	jne    16f0 <__libc_csu_init+0x40>
    1706:	48 83 c4 08          	add    $0x8,%rsp
    170a:	5b                   	pop    %rbx
    170b:	5d                   	pop    %rbp
    170c:	41 5c                	pop    %r12
    170e:	41 5d                	pop    %r13
    1710:	41 5e                	pop    %r14
    1712:	41 5f                	pop    %r15
    1714:	c3                   	ret    
    1715:	66 66 2e 0f 1f 84 00 	data16 cs nopw 0x0(%rax,%rax,1)
    171c:	00 00 00 00 

0000000000001720 <__libc_csu_fini>:
    1720:	f3 0f 1e fa          	endbr64 
    1724:	c3                   	ret    

Disassembly of section .fini:

0000000000001728 <_fini>:
    1728:	f3 0f 1e fa          	endbr64 
    172c:	48 83 ec 08          	sub    $0x8,%rsp
    1730:	48 83 c4 08          	add    $0x8,%rsp
    1734:	c3                   	ret    
