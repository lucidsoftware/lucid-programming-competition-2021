## Problem Statement

A diver is exploring a cavern, represented as a 2D m x n array. He can only move **vertically** or **across**. In the cavern array that is given as input, three possibilities for a given location are represented by three numbers: 
1. A **cave area** (represented as 2147483647, which is the maximum 32-bit integer value)
2. A **wall** (represented as -1) 
3. A **cave entrance** (represented as 0) that leads to the next cave. 

Output a 2D m x n array that represents the distance he will have to swim from any given **cave area** to the closest **cave entrance**. Leave any walls as -1 (because our diver cannot be inside a wall). Assume that if the diver is at a cave entrance he has to swim 0 units. Assume that if a diver cannot reach a **cave area** it remains the same value in the matrix (2147483647).

### Example input #1:
```
m = 6
n = 5
[[-1            -1            2147483647    -1            -1]
 [-1            2147483647    2147483647    -1            -1]
 [-1            2147483647    0             2147483647    -1]
 [-1            2147483647    2147483647    2147483647    -1]
 [-1            0             2147483647    2147483647    -1]
 [-1            2147483647    -1            2147483647    -1]]
```

### Example output #1:
```
[[-1            -1           2            -1            -1]
 [-1            2            1            -1            -1]
 [-1            1            0            1             -1]
 [-1            1            1            2             -1]
 [-1            0            1            2             -1]
 [-1            1            -1           3             -1]]
 ```

### Example input #2:
```
m = 2
n = 2
[[0            2147483647]
 [2147483647    2147483647]]
 ```

### Example output #2:
```
[[0            1]
 [1            2]]
```