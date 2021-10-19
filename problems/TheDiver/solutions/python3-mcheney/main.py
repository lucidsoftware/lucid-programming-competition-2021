M = int(input())
N = int(input())
cave = []
for m in range(M):
    cave.append([int(ea) for ea in input().split(' ')])

# find zeros
zeros = [(m, n) for m in range(M) for n in range(N) if cave[m][n] == 0]

from collections import deque
q = deque()

for _m, _n in zeros:
    q.append(((_m - 1, _n), 1))
    q.append(((_m + 1, _n), 1))
    q.append(((_m, _n - 1), 1))
    q.append(((_m, _n + 1), 1))

while len(q) > 0:
    (_m, _n), d = q.popleft()
    if _m < 0 or _n < 0 or _m >= M or _n >= N:
        continue
    if cave[_m][_n] == -1:
        continue
    if cave[_m][_n] == 0:
        continue
    if d <= cave[_m][_n]:
        cave[_m][_n] = d
        q.append(((_m - 1, _n), d + 1))
        q.append(((_m + 1, _n), d + 1))
        q.append(((_m, _n - 1), d + 1))
        q.append(((_m, _n + 1), d + 1))

for row in cave:
    print(*row)

