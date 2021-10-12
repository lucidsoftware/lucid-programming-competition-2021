def get_matrix(m):
    input_matrix = []
    i = 0
    while i < m:
        line = input()
        str_array = line.split(" ")
        output = list(map(lambda item: int(item), str_array))
        input_matrix += [output]
        i += 1
    return input_matrix

def diverSolution():
    m = int(input())
    n = int(input())
    input_matrix = get_matrix(m)
    CAVE_ENTRANCE = 0
    if m == 0 or n == 0:
        return []
    
    def dfs(x, y, distance):
        if x < 0 or x >= m or y < 0 or y >= n or input_matrix[x][y] < distance:
            return
        input_matrix[x][y] = distance
        dfs(x + 1, y, distance + 1)
        dfs(x, y + 1, distance + 1)
        dfs(x - 1, y, distance + 1)
        dfs(x, y - 1, distance + 1)

    for i in range(m):
        for j in range(n):
            if input_matrix[i][j] is CAVE_ENTRANCE:
                dfs(i, j, 0)
    return input_matrix

output_matrix = diverSolution();
for i in range(len(output_matrix)):
    print(*output_matrix[i], sep=' ')
