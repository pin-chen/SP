with open('d_rev.txt', 'r') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

d = 0
for line in lines:
    if "r = r * a % c" in line:
        d += 1
    elif "b >>= 1" in line:
        d <<= 1
        
print(d)