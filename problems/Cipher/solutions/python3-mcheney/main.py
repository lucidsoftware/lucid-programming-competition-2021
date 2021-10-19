C = int(input())
colOrder = [int(ea) - 1 for ea in input().split(' ')]
msg = input()
cols = ['' for _ in range(C)]
i = 0
for c in msg:
    cols[i] += c
    i += 1
    i %= C
for col in colOrder:
    print(cols[col], end='')
print('')
