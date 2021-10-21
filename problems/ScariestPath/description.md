## Problem Statement

A strange neighborhood has a collection of haunted houses, and visitors will come to this neighborhood and try to find the scariest order to visit the haunted houses. When visitors go into these haunted houses, they get scared in a unique way. They know how scary a house is after they visit it, and so they also get scared by the neighboring houses which they have already visited when they enter a haunted house.

There are `n` houses in this neighborhood, and house `i` will scare any visitor `scariness[i]` many times.
Haunted house `i` is a neighbor of haunted house `j` if `adjacency[i][j]` is `1`, and is not a neighbor otherwise.
When a visitor goes into a haunted house, they get scared as many times as that house scares them, and additionally get scared equal to the sum of the adjacent houses' scariness values which they have visited.

For a given collection of scariness values and adjacencies, what is the maximum number of times that a visitor can be scared while visiting?

## Interpreting the Input
The input consists of the number of houses `n`, the list of scariness values for the houses, and an `n` by `n` adjacency matrix.
The `i`th value in the list of scariness values describes the scariness value of the `i`th house.
The value in the `i`th row and `j`th column of the adjacency matrix is `1` if house `i` is neighbors with house `j`.
The input will be formatted in the following way:

```
n
x x x x x x <n length list with values separated by spaces>
0 0 0 0 0 0
0 0 0 0 0 0 <n x n input matrix with values separated by spaces>
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
```

## Output
Output an integer describing the maximum number of times a visitor can be scared by visiting each house once.

## Input Constraints
```
0 < n <= 100
0 < scariness[i] < 1000
```
`n` and all scariness values will be positive integers.

### Example Input #1:
```
3
1 2 3
0 1 1
1 0 0
1 0 0
```

### Example Output #1:
```
11
```
A visitor can be scared at most 11 times.

One order of visiting houses that could achieve this is visiting house 2, then house 1, then house 0.

At house 2, the visitor gets scared 3 times by the house itself. They have not visited any neighboring houses, so they are scared 3 times in total.

At house 1, the visitor gets scared 2 times by the house itself. They have not visited any neighboring houses, so they are scared 3 times in total.

At house 0, the visit gets scared 1 time by the house itself. They have visited both house 1 and house 2, which are adjacent, and so they are scared 5 times by these neighboring houses, for a total of 6 times while visiting house 0.

Thus, they have been scared `6 + 3 + 2 = 11` times in total.

### Example Input #2:
```
4
4 4 4 10
0 1 1 1
1 0 1 0
1 1 0 0
1 0 0 0
```

### Example Output #2:
```
44
```
A visitor can be scared at most 44 times.

One order that can achieve this is [3, 1, 0, 2].

At house 3, the visitor gets scared 10 times by the house itself. They have not visited any neighboring houses, so they are scared 10 times in total.

At house 1, the visitor gets scared 4 times by the house itself. They have not visited any neighboring houses, so they are scared 4 times in total.

At house 0, the visitor gets scared 4 times by the house itself. They have visited houses 1 and 3, so they are scared 10 times by house 3 and 4 times by house 1. They are scared 18 times in total.

At house 2, the visitor gets scared 4 times by the house itself. They have visited houses 0 and 1, so they are scared 4 times by each. They are scared 12 times in total.

Thus, the visitor is scared `10 + 4 + 18 + 12 = 44` times in total.
