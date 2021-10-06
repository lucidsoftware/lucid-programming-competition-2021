# Map Shortcut
## Description
You and your friends have discovered a treasure map leading to a trove of buried treasure. Your friends are planning on following each step of the map until they reach the treasure at the end. However, you would rather not share the treasure with your entire group of friends. Instead of following each step of the map, you want to first determine exactly where the treasure is buried, so you can go there directly. 
## Input
```
N
<Direction> <Degrees> <Paces>
<Direction> <Degrees> <Paces>
<Direction> <Degrees> <Paces>
…
```

### Where
* `N`: number of steps in the map, where one step includes the direction, the angle to turn in degrees, and the number of paces to take forward
* `Direction`: Left or Right
* `Degrees`: Number of degrees to turn in the given direction
* `Paces`: Number of paces to walk forward

### Example:
```
3
Right 90 20
Left 15 10
Left 135 15
```
 
## Output
Your output will look like the following:
```
Direction Degrees Paces
```

### Where:
* `Direction`: Right or Left
* `Degrees`: the number of degrees the user turns to face the endpoint
* `Paces`: the number of paces a user must travel to reach the endpoint

For your final answer, the user will never have to turn exactly 180 degrees. They should always turn less than 180 degrees. Therefore, if the endpoint is 10 paces away, directly to the right of the user, you should output:
```
Right 90 10
```
Rather than:
```
Left 270 10
```
The angle to turn and the number of paces to take should be rounded to the nearest whole number.
## Constraints
```
0 < N <= 10000
0 < Paces <= 100
0 < Degrees <= 180
```
Number of paces and angle to turn given in the input will always be integers
The final direction to take will never be exactly 0 degrees or exactly 180 degrees
The final number of paces you need to travel will always be greater than 1
## Examples
### Input 1
```
4
Left 90 10
Right 90 10
Right 90 20
Right 90 10
```
 
### Output 1
```
Right 90 10
```
 
### Input 2
```
4
Right 60 10
Right 120 10
Right 120 20
Left 120 10
```
### Output 2
```
Left 120 10
```
