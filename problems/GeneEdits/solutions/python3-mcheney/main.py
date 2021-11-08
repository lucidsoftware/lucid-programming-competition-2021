G = input()
E = int(input())

digits = set('0123456789')

i = 0
added, deleted = 0, 0


res = ''

for e in range(E):
    ind, op = input().split(' ')
    ind = int(ind)
    while i < ind + deleted - added and i < len(G):
        res += G[i]
        i += 1
    if set(op).issubset(digits):
        # Deletion
        op = int(op)
        i += op
        deleted += op
    else:
        # Insertion
        res += op
        added += len(op)

res += G[i:]

print(res)
