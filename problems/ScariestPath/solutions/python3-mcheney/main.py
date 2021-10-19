N = int(input())

weight = [int(ea) for ea in input().split(' ')]
weightWithIndex = [(i, w) for i, w in enumerate(weight)]
weightWithIndex.sort(key=lambda x: x[1], reverse=True)
adjMatrix = []
for n in range(N):
    adjMatrix.append([int(ea) for ea in input().split(' ')])

adjList = {n: set() for n in range(N)}
for n in range(N):
    for m in range(N):
        if adjMatrix[n][m]:
            adjList[n].add(m)

visited = set()
score = 0
for i, w in weightWithIndex:
    score += w
    for neighbor in adjList[i]:
        if neighbor in visited:
            score += weight[neighbor]
    visited.add(i)

print(score)

