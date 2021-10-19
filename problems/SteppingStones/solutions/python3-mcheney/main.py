from collections import deque

M, N = [int(ea) for ea in input().split(' ')]
floodOrder = list()
floodOrder.append(tuple())
for i in range(M * N):
    floodOrder.append(tuple(int(ea) - 1 for ea in input().split(' ')))


def solve(matr):
    q = deque()
    for m in range(M):
        q.append((m, 0))
    visited = set()
    while len(q) > 0:
        row, col = q.popleft()
        if (row, col) in visited:
            continue
        visited.add((row,col))
        if row < 0 or col < 0 or row >= M or col >= N:
            continue
        if matr[row][col] == 0:
            continue
        if col == N - 1:
            return True
        q.append((row+1, col))
        q.append((row-1, col))
        q.append((row, col+1))
        q.append((row, col-1))
    return False


pivot = (N * M) // 2
nextChange = (N * M) // 2


def setupMatrix(ICutoff):
    newMatrix = [[1 for n in range(N)] for m in range(M)]
    for i2 in range(ICutoff + 1):
        if len(floodOrder[i2]) > 0:
            newMatrix[floodOrder[i2][0]][floodOrder[i2][1]] = 0
    return newMatrix


pathExists = False
while True:
    # Test the pivot
    pathExists = solve(setupMatrix(pivot))
    # If passes, make it higher
    if nextChange == 0:
        break
    if nextChange == 0:
        break
    if pathExists:
        pivot += nextChange
    # If fails, make it lower
    else:
        pivot -= nextChange
    nextChange //= 2

while not pathExists:
    pivot -= 1
    pathExists = solve(setupMatrix(pivot))

while pathExists:
    pivot += 1
    pathExists = solve(setupMatrix(pivot))
pivot -= 1

print(pivot)
