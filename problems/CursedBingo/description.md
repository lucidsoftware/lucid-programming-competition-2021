# Cursed Bingo

You have been cursed with bad luck.  And your friends who are sadistic twerps take advantage of this by always playing games of chance with you.  Today they are playing Bingo.  You want to know how badly you are going to lose.

Given an `N` by `N` Bingo board, how many spots is it possible to fill without getting a Bingo?

## Definitions

A "Bingo" refers to having N spaces filled with a fixed offset between each of them of no more than ±1 in each dimension, which is adjacent to two parallel edges of the board.

That is, a Bingo is accomplished by filling in all of the spaces in one of the `N` columns, `N` rows, or 2 diagonals.

## Input

The first line of input will be an integer `L`.
The next `L` lines of input will be an integer `N`.

## Output

For each value of `N`, output the maximum number of spaces which can be filled in without a Bingo.

## Constraints
```
1 <= L < 1000
4 <= N <= 2000000
```

## Examples

### Input 0

```
1
5
```

### Output 0

```
20
```

### Explanation 0

One such unlucky board might look like the following:
|x|x|x|x| |
| |x|x|x|x|
|x| |x|x|x|
|x|x|x| |x|
|x|x| |x|x|

Which contains 20 filled spaces.

### Input 1

```
5
4
7
10
15
6
```

### Output 1

```
12
42
90
210
30
```