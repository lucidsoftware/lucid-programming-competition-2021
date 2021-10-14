# Assume we get list of numbers, and list of list of numbers

def process_input():
    n = int(input())
    lst = [int(x) for x in input().split(" ")]
    matrix = []
    for _ in range(n):
        matrix.append([int(x) for x in input().split(" ")])

    return lst, matrix

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

if __name__ == '__main__':
    scariness, adjacency = process_input()
    print(solution(scariness, adjacency))
