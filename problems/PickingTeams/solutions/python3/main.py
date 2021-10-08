"""
Everyone starts pointing to their own meta-team (name prefixed w/ _)

Claiming scenarios:
1. claimed has been stolen
    Do nothing
2. claimed has been claimed (i.e. this is stealing)
    Transfer and meta-team is parent
3. claimed is fresh
    Transfer and claimer is parent
"""

claimed = set()
stolen = set()
parent = dict()
children = dict()


def stealStudent(tar, metaParent):
    # All children must be non-stolen
    for child in children[tar]:
        stealStudent(child, metaParent)
    children[tar] = set()
    parent[tar] = metaParent
    children[metaParent].add(tar)
    stolen.add(tar)


def handleClaim(a, b):
    if b in stolen:
        return
    elif b in claimed:
        # This is stealing - transfer b to a's meta-parent
        # None of b's children should be stolen here, so transfer all of them
        # They will all become stolen
        metaParent = a
        while metaParent != parent[metaParent]:
            metaParent = parent[metaParent]
        stealStudent(b, metaParent)
        return
    else: # b is fresh
        # fresh will always be direct child of meta-parent
        children[parent[b]].remove(b)
        parent[b] = a
        children[a].add(b)
        claimed.add(b)
        # if b has children, steal them
        if len(children[b]) > 0:
            metaParent = a
            while metaParent != parent[metaParent]:
                metaParent = parent[metaParent]
            for ea in children[b]:
                stealStudent(ea, metaParent)
            children[b] = set()
        return


def handleQuery(a, b):
    metaParentA = a
    while metaParentA != parent[metaParentA]:
        metaParentA = parent[metaParentA]
    metaParentB = b
    while metaParentB != parent[metaParentB]:
        metaParentB = parent[metaParentB]
    print('yes' if metaParentA == metaParentB else 'no')


####### Process input #######

N = int(input())

for n in range(N):
    op, A, B = input().split(' ')
    if A not in parent:
        parent[A] = '_' + A
        parent['_' + A] = '_' + A
        children[A] = set()
        children['_' + A] = {A}

    if B not in parent:
        parent[B] = '_' + B
        parent['_' + B] = '_' + B
        children[B] = set()
        children['_' + B] = {B}

    if op == '+':
        handleClaim(A, B)
    else:
        handleQuery(A, B)

print(len([ea for ea in parent if ea.startswith('_') and len(children[ea]) > 0]))