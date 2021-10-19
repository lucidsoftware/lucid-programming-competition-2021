from collections import deque

N = int(input())
parent = dict()
children = dict()
stolen = set()
claimed = set()
for n in range(N):
    op, A, B = input().split(' ')

    if A not in parent:
        parent[A] = f'_{A}'
        parent[f'_{A}'] = f'_{A}'
        children[A] = set()
        children[f'_{A}'] = {A}
    if B not in parent:
        parent[B] = f'_{B}'
        parent[f'_{B}'] = f'_{B}'
        children[B] = set()
        children[f'_{B}'] = {B}

    topParentA = parent[A]
    while topParentA != parent[topParentA]:
        topParentA = parent[topParentA]
    topParentB = parent[B]
    while topParentB != parent[topParentB]:
        topParentB = parent[topParentB]

    if op == '+':
        if topParentA == topParentB:
            continue
        # Process add command
        if B in stolen:
            continue
        q = deque()
        q.append(B)
        while len(q) > 0:
            nxt = q.popleft()
            if nxt in stolen:
                continue
            if nxt in children[parent[nxt]]: children[parent[nxt]].remove(nxt)
            if nxt in claimed:
                parent[nxt] = topParentA
                children[topParentA].add(nxt)
                stolen.add(nxt)
            else:
                parent[nxt] = A
                children[A].add(nxt)
                claimed.add(nxt)
            for child in children[nxt]:
                q.append(child)
            children[nxt] = set()
    else:
        # Process query
        print('yes' if topParentA == topParentB else 'no')
print(len([par for par, chil in children.items() if par.startswith('_') and len(chil) > 0]))
