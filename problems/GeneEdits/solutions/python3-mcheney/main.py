import sys

G = input()
E = int(input())

digits = set('0123456789')

i = 0
added, deleted = 0, 0


def p(arg):
    sys.stdout.write(arg)


for e in range(E):
    ind, op = input().split(' ')
    ind = int(ind)
    while i < ind + deleted - added and i < len(G):
        p(G[i])
        i += 1
    if set(op).issubset(digits):
        # Deletion
        op = int(op)
        i += op
        deleted += op
    else:
        # Insertion
        p(op)
        if i < len(G):
            p(G[i])
        i += 1
        added += len(op)

while i < len(G):
    p(G[i])
    i += 1

sys.stdout.write('\n')
sys.stdout.flush()

