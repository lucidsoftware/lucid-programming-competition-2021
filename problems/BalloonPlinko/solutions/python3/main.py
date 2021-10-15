import math

def process_input():
    n = int(input())
    balloons = []
    for _ in range(n):
        balloons.append([int(x) for x in input().split(' ')])
    return balloons

# The Euclidean distance from (x1, y1) to (x2, y2)
def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** .5

def distance_3d(x1, y1, z1, x2, y2, z2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** .5

# Projects (x, y) directly away from (x_c, y_c) to a distance of r
def project_to_edge(x, y, x_c, y_c, r):
    dx = x - x_c
    dy = y - y_c
    size = distance(dx, dy, 0, 0)
    x_f = (dx / size) * r
    y_f = (dy / size) * r
    return x_c + x_f, y_c + y_f

def check_balloons(balloons):
    for i in range(len(balloons)):
        x1, y1, z1, r1 = balloons[i]
        for j in range(len(balloons)):
            x2, y2, z2, r2 = balloons[j]
            if i != j and distance_3d(x1, y1, z1, x2, y2, z2) < r1 + r2:
                print("Overlap between balloons.\n%d %d %d %d\n %d %d %d %d" % (x1, y1, z1, r1, x2, y2, z2, r2))

def solution(balloons):
    # Starting at height 1000
    balloons.sort(reverse=True, key=lambda x: x[2])
    h = 100
    x = 0
    y = 0
    for bx, by, bh, r in balloons:
        if distance(x, y, bx, by) < r:
            x, y = project_to_edge(x, y, bx, by, r)

    return math.ceil(x), math.ceil(y)

def print_solution(x, y):
    print("%d %d" % (x, y))


if __name__ == '__main__':
    balloons = process_input()
    print_solution(*solution(balloons))
