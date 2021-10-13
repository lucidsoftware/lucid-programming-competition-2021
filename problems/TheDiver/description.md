## Problem Statement

A diver is exploring a cavern, represented as a 2D n x m array (m rows, n columns). He can only move **vertically** or **across**. In the cavern array that is given as input, three possibilities for a given location are represented by three numbers: 
1. A **cave area** (represented as 2147483647, which is the maximum 32-bit integer value)
2. A **wall** (represented as -1) 
3. A **cave entrance** (represented as 0) that leads to the next cave. 


## Interpreting the Input
The input will be formatted in the following way:

```
m
n
0 0 0 0 0
0 0 0 0 0 <n x m input matrix with values separated with spaces>
0 0 0 0 0
```

The matrix is therefore **m rows tall** and **n rows wide**.

## Output
Output a 2D n x m array that represents the distance he will have to swim from any given **cave area** to the closest **cave entrance**. Leave any **walls** as -1 (because our diver cannot be inside a wall). Assume that if the diver is at a **cave entrance** he has to swim 0 units. Assume that if a diver cannot reach a **cave area** it remains the same value in the matrix (2147483647). **Your output matrix should be formatted the same as the input matrix.**

### Example input #1:
```
6
5
-1 -1 2147483647 -1 -1
-1 2147483647 2147483647 -1 -1
-1 2147483647 0 2147483647 -1
-1 2147483647 2147483647 2147483647 -1
-1 0 2147483647 2147483647 -1
-1 2147483647 -1 2147483647 -1
```

### Example output #1:
```
-1 -1 2 -1 -1
-1 2 1 -1 -1
-1 1 0 1 -1
-1 1 1 2 -1
-1 0 1 2 -1
-1 1 -1 3 -1
 ```

### Example input #2:
```
2
2
0 2147483647
2147483647 2147483647
 ```

### Example output #2:
```
0 1
1 2
```
