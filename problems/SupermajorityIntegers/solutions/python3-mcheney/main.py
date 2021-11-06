N = int(input())

d = dict()

for n in range(N):
    i = int(input())
    if i not in d:
        d[i] = 0
    d[i] += 1

mostFreq = sorted([v for k, v in d.items()], reverse=True)[0]
print(True if mostFreq > (2 * N) / 3 else False)

