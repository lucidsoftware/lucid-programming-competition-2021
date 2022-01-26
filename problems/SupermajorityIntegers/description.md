# Supermajority Integers

Given a list of integers, you want to know whether more than 2/3 of the integers in the list are the same.

Write a program that prints "True" or "False" according to whether more than 2/3 of the integers in a given list are the same.

## Input
As input, you will receive the following:

* The number of integers in the list.
* An integer in the list to process.

The input will be formatted as follows:
```
<number of integers in list, m>
<integer 1>
<integer 2>
...
<integer i>
```

## Output
Output the string "True" or "False", whether more than 2/3 of the integers in a list are the same in the list, as follows:
```
False
```

```
True
```

## Constraints
* Where `m` is the number of integers, `1 <= m <= 1000`
* Where `s` is an integer in the list, `0 <= s <= 10000`

## Examples

### Input 0
```
4
2
3
1
0
```

### Output 0
```
False
```

### Input 1
```
4
0
0
1
0
```

### Output 1
```
False
```

### Input 2
```
5
3
2
3
3
3
```

### Output 2
```
True
```
