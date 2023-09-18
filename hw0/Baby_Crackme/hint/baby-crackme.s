
baby-crackme:     file format elf64-x86-64


Disassembly of section .init:

0000000000001000 <.init>:
    1000:	f3 0f 1e fa          	endbr64 
    1004:	48 83 ec 08          	sub    $0x8,%rsp
    1008:	48 8b 05 d9 2f 00 00 	mov    0x2fd9(%rip),%rax        # 3fe8 <__isoc99_scanf@plt+0x2f18>
    100f:	48 85 c0             	test   %rax,%rax
    1012:	74 02                	je     1016 <__cxa_finalize@plt-0x6a>
    1014:	ff d0                	call   *%rax
    1016:	48 83 c4 08          	add    $0x8,%rsp
    101a:	c3                   	ret    

Disassembly of section .plt:

0000000000001020 <.plt>:
    1020:	ff 35 7a 2f 00 00    	push   0x2f7a(%rip)        # 3fa0 <__isoc99_scanf@plt+0x2ed0>
    1026:	f2 ff 25 7b 2f 00 00 	bnd jmp *0x2f7b(%rip)        # 3fa8 <__isoc99_scanf@plt+0x2ed8>
    102d:	0f 1f 00             	nopl   (%rax)
    1030:	f3 0f 1e fa          	endbr64 
    1034:	68 00 00 00 00       	push   $0x0
    1039:	f2 e9 e1 ff ff ff    	bnd jmp 1020 <__cxa_finalize@plt-0x60>
    103f:	90                   	nop
    1040:	f3 0f 1e fa          	endbr64 
    1044:	68 01 00 00 00       	push   $0x1
    1049:	f2 e9 d1 ff ff ff    	bnd jmp 1020 <__cxa_finalize@plt-0x60>
    104f:	90                   	nop
    1050:	f3 0f 1e fa          	endbr64 
    1054:	68 02 00 00 00       	push   $0x2
    1059:	f2 e9 c1 ff ff ff    	bnd jmp 1020 <__cxa_finalize@plt-0x60>
    105f:	90                   	nop
    1060:	f3 0f 1e fa          	endbr64 
    1064:	68 03 00 00 00       	push   $0x3
    1069:	f2 e9 b1 ff ff ff    	bnd jmp 1020 <__cxa_finalize@plt-0x60>
    106f:	90                   	nop
    1070:	f3 0f 1e fa          	endbr64 
    1074:	68 04 00 00 00       	push   $0x4
    1079:	f2 e9 a1 ff ff ff    	bnd jmp 1020 <__cxa_finalize@plt-0x60>
    107f:	90                   	nop

Disassembly of section .plt.got:

0000000000001080 <__cxa_finalize@plt>:
    1080:	f3 0f 1e fa          	endbr64 
    1084:	f2 ff 25 6d 2f 00 00 	bnd jmp *0x2f6d(%rip)        # 3ff8 <__isoc99_scanf@plt+0x2f28>
    108b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

Disassembly of section .plt.sec:

0000000000001090 <puts@plt>:
    1090:	f3 0f 1e fa          	endbr64 
    1094:	f2 ff 25 15 2f 00 00 	bnd jmp *0x2f15(%rip)        # 3fb0 <__isoc99_scanf@plt+0x2ee0>
    109b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

00000000000010a0 <__stack_chk_fail@plt>:
    10a0:	f3 0f 1e fa          	endbr64 
    10a4:	f2 ff 25 0d 2f 00 00 	bnd jmp *0x2f0d(%rip)        # 3fb8 <__isoc99_scanf@plt+0x2ee8>
    10ab:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

00000000000010b0 <printf@plt>:
    10b0:	f3 0f 1e fa          	endbr64 
    10b4:	f2 ff 25 05 2f 00 00 	bnd jmp *0x2f05(%rip)        # 3fc0 <__isoc99_scanf@plt+0x2ef0>
    10bb:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

00000000000010c0 <strcmp@plt>:
    10c0:	f3 0f 1e fa          	endbr64 
    10c4:	f2 ff 25 fd 2e 00 00 	bnd jmp *0x2efd(%rip)        # 3fc8 <__isoc99_scanf@plt+0x2ef8>
    10cb:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

00000000000010d0 <__isoc99_scanf@plt>:
    10d0:	f3 0f 1e fa          	endbr64 
    10d4:	f2 ff 25 f5 2e 00 00 	bnd jmp *0x2ef5(%rip)        # 3fd0 <__isoc99_scanf@plt+0x2f00>
    10db:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

Disassembly of section .text:

00000000000010e0 <.text>:
    10e0:	f3 0f 1e fa          	endbr64 
    10e4:	31 ed                	xor    %ebp,%ebp
    10e6:	49 89 d1             	mov    %rdx,%r9
    10e9:	5e                   	pop    %rsi
    10ea:	48 89 e2             	mov    %rsp,%rdx
    10ed:	48 83 e4 f0          	and    $0xfffffffffffffff0,%rsp
    10f1:	50                   	push   %rax
    10f2:	54                   	push   %rsp
    10f3:	45 31 c0             	xor    %r8d,%r8d
    10f6:	31 c9                	xor    %ecx,%ecx
    10f8:	48 8d 3d 93 01 00 00 	lea    0x193(%rip),%rdi        # 1292 <__isoc99_scanf@plt+0x1c2>
    10ff:	ff 15 d3 2e 00 00    	call   *0x2ed3(%rip)        # 3fd8 <__isoc99_scanf@plt+0x2f08>
    1105:	f4                   	hlt    
    1106:	66 2e 0f 1f 84 00 00 	cs nopw 0x0(%rax,%rax,1)
    110d:	00 00 00 
    1110:	48 8d 3d f9 2e 00 00 	lea    0x2ef9(%rip),%rdi        # 4010 <__isoc99_scanf@plt+0x2f40>
    1117:	48 8d 05 f2 2e 00 00 	lea    0x2ef2(%rip),%rax        # 4010 <__isoc99_scanf@plt+0x2f40>
    111e:	48 39 f8             	cmp    %rdi,%rax
    1121:	74 15                	je     1138 <__isoc99_scanf@plt+0x68>
    1123:	48 8b 05 b6 2e 00 00 	mov    0x2eb6(%rip),%rax        # 3fe0 <__isoc99_scanf@plt+0x2f10>
    112a:	48 85 c0             	test   %rax,%rax
    112d:	74 09                	je     1138 <__isoc99_scanf@plt+0x68>
    112f:	ff e0                	jmp    *%rax
    1131:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
    1138:	c3                   	ret    
    1139:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
    1140:	48 8d 3d c9 2e 00 00 	lea    0x2ec9(%rip),%rdi        # 4010 <__isoc99_scanf@plt+0x2f40>
    1147:	48 8d 35 c2 2e 00 00 	lea    0x2ec2(%rip),%rsi        # 4010 <__isoc99_scanf@plt+0x2f40>
    114e:	48 29 fe             	sub    %rdi,%rsi
    1151:	48 89 f0             	mov    %rsi,%rax
    1154:	48 c1 ee 3f          	shr    $0x3f,%rsi
    1158:	48 c1 f8 03          	sar    $0x3,%rax
    115c:	48 01 c6             	add    %rax,%rsi
    115f:	48 d1 fe             	sar    %rsi
    1162:	74 14                	je     1178 <__isoc99_scanf@plt+0xa8>
    1164:	48 8b 05 85 2e 00 00 	mov    0x2e85(%rip),%rax        # 3ff0 <__isoc99_scanf@plt+0x2f20>
    116b:	48 85 c0             	test   %rax,%rax
    116e:	74 08                	je     1178 <__isoc99_scanf@plt+0xa8>
    1170:	ff e0                	jmp    *%rax
    1172:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
    1178:	c3                   	ret    
    1179:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
    1180:	f3 0f 1e fa          	endbr64 
    1184:	80 3d 85 2e 00 00 00 	cmpb   $0x0,0x2e85(%rip)        # 4010 <__isoc99_scanf@plt+0x2f40>
    118b:	75 2b                	jne    11b8 <__isoc99_scanf@plt+0xe8>
    118d:	55                   	push   %rbp
    118e:	48 83 3d 62 2e 00 00 	cmpq   $0x0,0x2e62(%rip)        # 3ff8 <__isoc99_scanf@plt+0x2f28>
    1195:	00 
    1196:	48 89 e5             	mov    %rsp,%rbp
    1199:	74 0c                	je     11a7 <__isoc99_scanf@plt+0xd7>
    119b:	48 8b 3d 66 2e 00 00 	mov    0x2e66(%rip),%rdi        # 4008 <__isoc99_scanf@plt+0x2f38>
    11a2:	e8 d9 fe ff ff       	call   1080 <__cxa_finalize@plt>
    11a7:	e8 64 ff ff ff       	call   1110 <__isoc99_scanf@plt+0x40>
    11ac:	c6 05 5d 2e 00 00 01 	movb   $0x1,0x2e5d(%rip)        # 4010 <__isoc99_scanf@plt+0x2f40>
    11b3:	5d                   	pop    %rbp
    11b4:	c3                   	ret    
    11b5:	0f 1f 00             	nopl   (%rax)
    11b8:	c3                   	ret    
    11b9:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
    11c0:	f3 0f 1e fa          	endbr64 
    11c4:	e9 77 ff ff ff       	jmp    1140 <__isoc99_scanf@plt+0x70>
    11c9:	f3 0f 1e fa          	endbr64 
    11cd:	55                   	push   %rbp
    11ce:	48 89 e5             	mov    %rsp,%rbp
    11d1:	48 83 ec 50          	sub    $0x50,%rsp
    11d5:	48 89 7d b8          	mov    %rdi,-0x48(%rbp)
    11d9:	89 75 b4             	mov    %esi,-0x4c(%rbp)
    11dc:	89 55 b0             	mov    %edx,-0x50(%rbp)
    11df:	64 48 8b 04 25 28 00 	mov    %fs:0x28,%rax
    11e6:	00 00 
    11e8:	48 89 45 f8          	mov    %rax,-0x8(%rbp)
    11ec:	31 c0                	xor    %eax,%eax
    11ee:	48 c7 45 d0 00 00 00 	movq   $0x0,-0x30(%rbp)
    11f5:	00 
    11f6:	48 c7 45 d8 00 00 00 	movq   $0x0,-0x28(%rbp)
    11fd:	00 
    11fe:	48 c7 45 e0 00 00 00 	movq   $0x0,-0x20(%rbp)
    1205:	00 
    1206:	48 c7 45 e8 00 00 00 	movq   $0x0,-0x18(%rbp)
    120d:	00 
    120e:	c7 45 f0 00 00 00 00 	movl   $0x0,-0x10(%rbp)
    1215:	c7 45 cc 00 00 00 00 	movl   $0x0,-0x34(%rbp)
    121c:	eb 3b                	jmp    1259 <__isoc99_scanf@plt+0x189>
    121e:	8b 45 cc             	mov    -0x34(%rbp),%eax
    1221:	48 98                	cltq   
    1223:	48 8d 15 f6 0d 00 00 	lea    0xdf6(%rip),%rdx        # 2020 <__isoc99_scanf@plt+0xf50>
    122a:	0f b6 04 10          	movzbl (%rax,%rdx,1),%eax
    122e:	88 45 cb             	mov    %al,-0x35(%rbp)
    1231:	8b 45 b0             	mov    -0x50(%rbp),%eax
    1234:	32 45 cb             	xor    -0x35(%rbp),%al
    1237:	89 c2                	mov    %eax,%edx
    1239:	8b 45 cc             	mov    -0x34(%rbp),%eax
    123c:	48 98                	cltq   
    123e:	88 54 05 d0          	mov    %dl,-0x30(%rbp,%rax,1)
    1242:	d1 4d b0             	rorl   -0x50(%rbp)
    1245:	0f b6 45 cb          	movzbl -0x35(%rbp),%eax
    1249:	31 45 b0             	xor    %eax,-0x50(%rbp)
    124c:	8b 45 b4             	mov    -0x4c(%rbp),%eax
    124f:	2b 45 cc             	sub    -0x34(%rbp),%eax
    1252:	01 45 b0             	add    %eax,-0x50(%rbp)
    1255:	83 45 cc 01          	addl   $0x1,-0x34(%rbp)
    1259:	8b 45 cc             	mov    -0x34(%rbp),%eax
    125c:	3b 45 b4             	cmp    -0x4c(%rbp),%eax
    125f:	7c bd                	jl     121e <__isoc99_scanf@plt+0x14e>
    1261:	48 8b 55 b8          	mov    -0x48(%rbp),%rdx
    1265:	48 8d 45 d0          	lea    -0x30(%rbp),%rax
    1269:	48 89 d6             	mov    %rdx,%rsi
    126c:	48 89 c7             	mov    %rax,%rdi
    126f:	e8 4c fe ff ff       	call   10c0 <strcmp@plt>
    1274:	85 c0                	test   %eax,%eax
    1276:	0f 94 c0             	sete   %al
    1279:	0f b6 c0             	movzbl %al,%eax
    127c:	48 8b 55 f8          	mov    -0x8(%rbp),%rdx
    1280:	64 48 2b 14 25 28 00 	sub    %fs:0x28,%rdx
    1287:	00 00 
    1289:	74 05                	je     1290 <__isoc99_scanf@plt+0x1c0>
    128b:	e8 10 fe ff ff       	call   10a0 <__stack_chk_fail@plt>
    1290:	c9                   	leave  
    1291:	c3                   	ret    
    1292:	f3 0f 1e fa          	endbr64 
    1296:	55                   	push   %rbp
    1297:	48 89 e5             	mov    %rsp,%rbp
    129a:	48 83 ec 30          	sub    $0x30,%rsp
    129e:	64 48 8b 04 25 28 00 	mov    %fs:0x28,%rax
    12a5:	00 00 
    12a7:	48 89 45 f8          	mov    %rax,-0x8(%rbp)
    12ab:	31 c0                	xor    %eax,%eax
    12ad:	48 c7 45 d0 00 00 00 	movq   $0x0,-0x30(%rbp)
    12b4:	00 
    12b5:	48 c7 45 d8 00 00 00 	movq   $0x0,-0x28(%rbp)
    12bc:	00 
    12bd:	48 c7 45 e0 00 00 00 	movq   $0x0,-0x20(%rbp)
    12c4:	00 
    12c5:	48 c7 45 e8 00 00 00 	movq   $0x0,-0x18(%rbp)
    12cc:	00 
    12cd:	c7 45 f0 00 00 00 00 	movl   $0x0,-0x10(%rbp)
    12d4:	48 8d 05 6d 0d 00 00 	lea    0xd6d(%rip),%rax        # 2048 <__isoc99_scanf@plt+0xf78>
    12db:	48 89 c7             	mov    %rax,%rdi
    12de:	e8 ad fd ff ff       	call   1090 <puts@plt>
    12e3:	48 8d 05 8a 0d 00 00 	lea    0xd8a(%rip),%rax        # 2074 <__isoc99_scanf@plt+0xfa4>
    12ea:	48 89 c7             	mov    %rax,%rdi
    12ed:	b8 00 00 00 00       	mov    $0x0,%eax
    12f2:	e8 b9 fd ff ff       	call   10b0 <printf@plt>
    12f7:	48 8d 45 d0          	lea    -0x30(%rbp),%rax
    12fb:	48 89 c6             	mov    %rax,%rsi
    12fe:	48 8d 05 83 0d 00 00 	lea    0xd83(%rip),%rax        # 2088 <__isoc99_scanf@plt+0xfb8>
    1305:	48 89 c7             	mov    %rax,%rdi
    1308:	b8 00 00 00 00       	mov    $0x0,%eax
    130d:	e8 be fd ff ff       	call   10d0 <__isoc99_scanf@plt>
    1312:	48 8d 45 d0          	lea    -0x30(%rbp),%rax
    1316:	ba 0c b0 ce ba       	mov    $0xbaceb00c,%edx
    131b:	be 24 00 00 00       	mov    $0x24,%esi
    1320:	48 89 c7             	mov    %rax,%rdi
    1323:	e8 a1 fe ff ff       	call   11c9 <__isoc99_scanf@plt+0xf9>
    1328:	85 c0                	test   %eax,%eax
    132a:	74 11                	je     133d <__isoc99_scanf@plt+0x26d>
    132c:	48 8d 05 5a 0d 00 00 	lea    0xd5a(%rip),%rax        # 208d <__isoc99_scanf@plt+0xfbd>
    1333:	48 89 c7             	mov    %rax,%rdi
    1336:	e8 55 fd ff ff       	call   1090 <puts@plt>
    133b:	eb 0f                	jmp    134c <__isoc99_scanf@plt+0x27c>
    133d:	48 8d 05 58 0d 00 00 	lea    0xd58(%rip),%rax        # 209c <__isoc99_scanf@plt+0xfcc>
    1344:	48 89 c7             	mov    %rax,%rdi
    1347:	e8 44 fd ff ff       	call   1090 <puts@plt>
    134c:	b8 00 00 00 00       	mov    $0x0,%eax
    1351:	48 8b 55 f8          	mov    -0x8(%rbp),%rdx
    1355:	64 48 2b 14 25 28 00 	sub    %fs:0x28,%rdx
    135c:	00 00 
    135e:	74 05                	je     1365 <__isoc99_scanf@plt+0x295>
    1360:	e8 3b fd ff ff       	call   10a0 <__stack_chk_fail@plt>
    1365:	c9                   	leave  
    1366:	c3                   	ret    

Disassembly of section .fini:

0000000000001368 <.fini>:
    1368:	f3 0f 1e fa          	endbr64 
    136c:	48 83 ec 08          	sub    $0x8,%rsp
    1370:	48 83 c4 08          	add    $0x8,%rsp
    1374:	c3                   	ret    
