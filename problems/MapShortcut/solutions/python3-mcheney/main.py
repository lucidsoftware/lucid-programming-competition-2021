from math import asin, acos, degrees, cos, sin, atan, radians

N = int(input())

facing = 0
x, y = 0, 0
for n in range(N):
    line = input().split(' ')
    direction = line[0]
    deg = int(line[1])
    paces = int(line[2])
    if direction == 'Left':
        facing += deg
    else:
        facing -= deg
    facing %= 360

    if facing < 90:
        angleToUse = facing
    elif facing < 180:
        angleToUse = 180 - facing
    elif facing < 270:
        angleToUse = facing - 180
    else:
        angleToUse = 360 - facing

    if facing == 0:
        dx = paces
        dy = 0
    elif facing == 90:
        dx = 0
        dy = paces
    elif facing == 180:
        dx = -paces
        dy = 0
    elif facing == 270:
        dx = 0
        dy = -paces
    else:
        # use asin and acos
        dx = paces * cos(radians(angleToUse))
        dy = paces * sin(radians(angleToUse))
        if facing < 90:
            pass
        elif facing < 180:
            dx = -dx
        elif facing < 270:
            dx = -dx
            dy = -dy
        else:
            dy = -dy
    x += dx
    y += dy


dist = round((y**2 + x**2) ** .5)

if x == 0 and y > 0:
    print(f'Left 90 {dist}')
elif x == 0 and y < 0:
    print(f'Right 90 {dist}')
elif y == 0 and x > 0:
    print(f'Left 0 {dist}')
elif y == 0 and x < 0:
    print(f'Left 180 {dist}')
else:
    angleToTurn = round(abs(degrees(atan(y / x))))
    if x > 0 and y > 0:
        print(f'Left {angleToTurn} {dist}')
    elif x < 0 and y > 0:
        print(f'Left {180 - angleToTurn} {dist}')
    elif x < 0 and y < 0:
        print(f'Right {180 - angleToTurn} {dist}')
    else:
        print(f'Right {angleToTurn} {dist}')
