from pwn import *

r = process(['cat','k_target.txt'])

target = r.recv(43)

print(target)

a1 = list()

for i in range(43):
    a1.append(target[i])

a1[5] -= a1[37] + a1[20] 
a1[8] -= a1[14] + a1[16] 
a1[17] -= a1[38] + a1[24] 
a1[15] -= a1[40] + a1[8] 
a1[37] -= a1[12] + a1[16] 
a1[4] -= a1[6] + a1[22] 
a1[10] += a1[12] + a1[22]
a1[18] -= a1[26] + a1[31]
a1[23] -= a1[30] + a1[39]
a1[4] -= a1[27] + a1[25]
a1[37] -= a1[27] + a1[18]
a1[41] += a1[3] + a1[34]
a1[13] -= a1[26] + a1[8]
a1[2] -= a1[34] + a1[25]
a1[0] -= a1[28] + a1[31]
a1[4] -= a1[7] + a1[25]
a1[18] -= a1[29] + a1[15]
a1[21] += a1[13] + a1[42]
a1[21] -= a1[34] + a1[15]
a1[7] -= a1[10] + a1[0]
a1[13] -= a1[25] + a1[28]
a1[32] -= a1[5] + a1[25]
a1[31] -= a1[1] + a1[16]
a1[1] -= a1[16] + a1[40]
a1[30] += a1[13] + a1[2]
a1[1] -= a1[15] + a1[6]
a1[7] -= a1[21] + a1[0]
a1[24] -= a1[20] + a1[5]
a1[36] -= a1[11] + a1[15]
a1[0] -= a1[33] + a1[16]
a1[19] -= a1[10] + a1[16]
a1[1] += a1[29] + a1[13]
a1[30] += a1[33] + a1[8]
a1[15] -= a1[22] + a1[10]
a1[20] -= a1[19] + a1[24]
a1[27] -= a1[18] + a1[20]
a1[39] += a1[25] + a1[38]
a1[23] -= a1[7] + a1[34]
a1[37] += a1[29] + a1[3]
a1[5] -= a1[40] + a1[4]
a1[17] -= a1[0] + a1[7]
a1[9] -= a1[11] + a1[3]
a1[31] -= a1[34] + a1[16]
a1[16] -= a1[25] + a1[11]
a1[14] += a1[32] + a1[6]
a1[6] -= a1[10] + a1[41]
a1[2] -= a1[11] + a1[8]
a1[0] += a1[18] + a1[31]
a1[9] += a1[2] + a1[22]
a1[14] -= a1[35] + a1[8]

for i in range(43):
    print(chr(a1[i]%256),end='')