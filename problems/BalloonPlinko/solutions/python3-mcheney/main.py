import math
from math import sqrt

N = int(input())
balloons = []
for n in range(N):
    balloons.append([int(ea) for ea in input().split(' ')])
# x y z r
x, y = 0, 0

for bx, by, bz, br in sorted(balloons, key=lambda x: x[2], reverse=True):
    distToCenter = sqrt((bx - x)**2 + (by - y)**2)
    if distToCenter >= br:
        continue
    deltaX = x - bx
    deltaY = y - by
    x += (br - distToCenter) * (deltaX / distToCenter)
    y += (br - distToCenter) * (deltaY / distToCenter)

print(math.ceil(x), math.ceil(y))

