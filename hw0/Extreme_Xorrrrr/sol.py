from secret import flag
from Crypto.Util.number import bytes_to_long, getPrime, long_to_bytes, inverse
from functools import reduce

def xorrrrr(nums):
    n = len(nums)
    result = [0] * n
    for i in range(1, n):
        result = [ result[j] ^ nums[(j+i) % n] for j in range(n)]
    return result

def reverse_xorrrrr(nums):
    tmp = 0
    for num in nums:
        tmp ^= num
    result = [ nums[i] ^ tmp for i in range(len(nums))]
    return result

def egcd(a, b):
    if 0 == b:
        return 1, 0, a
    x, y, q = egcd(b, a % b)
    x, y = y, (x - a // b * y)
    return x, y, q

def chinese_remainder(pairs):
    mod_list, remainder_list = [p[0] for p in pairs], [p[1] for p in pairs]
    mod_product = reduce(lambda x, y: x * y, mod_list)
    mi_list = [mod_product // x for x in mod_list]
    mi_inverse = [egcd(mi_list[i], mod_list[i])[0] for i in range(len(mi_list))]
    x = 0
    for i in range(len(remainder_list)):
        x += mi_list[i] * mi_inverse[i] * remainder_list[i]
        x %= mod_product
    return x

hint = [297901710, 2438499757, 172983774, 2611781033, 2766983357, 1018346993, 810270522, 2334480195, 154508735, 1066271428, 3716430041, 875123909, 2664535551, 2193044963, 2538833821, 2856583708, 3081106896, 2195167145, 2811407927, 3794168460]
muls = [865741, 631045, 970663, 575787, 597689, 791331, 594479, 857481, 797931, 1006437, 661791, 681453, 963397, 667371, 705405, 684177, 736827, 757871, 698753, 841555]
mods = [2529754263, 4081964537, 2817833411, 3840103391, 3698869687, 3524873305, 2420253753, 2950766353, 3160043859, 2341042647, 4125137273, 3875984107, 4079282409, 2753416889, 2778711505, 3667413387, 4187196169, 3489959487, 2756285845, 3925748705]

hint = reverse_xorrrrr(hint)
muls = reverse_xorrrrr(muls)
mods = reverse_xorrrrr(mods)

num = [0] * 20

for i in range(20):
    num[i] = hint[i] * inverse(muls[i], mods[i]) % mods[i]

result = []
for i in range(20):
    result.append((mods[i], num[i]))

secret = chinese_remainder(result)

flag = long_to_bytes(secret).decode()

print(flag)