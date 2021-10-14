from networkx.linalg.graphmatrix import adjacency_matrix
from networkx.generators.random_graphs import erdos_renyi_graph
import numpy as np


def solution(scariness, adjacency):
    n = len(scariness)
    idxs = [i[0] for i in sorted(enumerate(scariness), key = lambda x: -x[1])]
    tot = 0
    seen = set()
    for i in range(n):
        idx = idxs[i]
        tot += scariness[idx]
        for j in range(n):
            if adjacency[idx][j] and j in seen:
                tot += scariness[j]
        seen.add(idx)
    return tot


n = 3
numvalues = 10
for i in range(n, 11):
    lst = np.random.randint(1, 1000, numvalues)
    g = erdos_renyi_graph(numvalues, .8 - .05 * n)
    adjacency = adjacency_matrix(g).toarray()
    ret = solution(lst, adjacency)
    with open('tests/%d.in' % n, 'w') as f:
        f.write('%d\n' % numvalues)
        f.write(' '.join([str(x) for x in lst]) + '\n')
        for i in range(numvalues):
            f.write(' '.join([str(x) for x in adjacency[i]]) + '\n')

    with open('tests/%d.out' % n, 'w') as f:
        f.write('%d\n' % ret)

    n += 1
    numvalues += 5
