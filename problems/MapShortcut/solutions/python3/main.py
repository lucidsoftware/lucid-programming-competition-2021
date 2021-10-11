import math

def toRadians(degrees):
    return degrees * math.pi / 180
    
def toDegrees(radians):
    return radians * 180 / math.pi


numberOfSteps = int(input())
location_x = 0
location_y = 0
facing = 0
for x in range(0, numberOfSteps):
    step = input().split()
    direction = step[0]
    angle = int(step[1])
    paces = int(step[2])
    if direction == "Right":
        angle = 360 - angle;
    facing = (facing + angle) % 360;
    location_x += math.cos(toRadians(facing)) * paces;
    location_y += math.sin(toRadians(facing)) * paces;
distance = math.sqrt((location_x * location_x) + (location_y * location_y));
heading = toDegrees(math.acos(location_x / distance));
print(("Left " if location_y > 0 else "Right ") + str(math.floor(heading + 0.5)) + " " + str(math.floor(distance + 0.5)))
