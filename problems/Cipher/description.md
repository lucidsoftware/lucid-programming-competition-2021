# Cipher

You've been exchanging secret messages with a friend, but the code you were using was cracked, so now you need to use a new one. You decide to use a grid to scramble your message.

You will write each character across a grid with a specified number of columns. You will then print the letters taken vertically from each column in the order specified for the columns to be taken.

For example, if you want to convert "Hello, world!" into your secret code using three columns, first you would write it out across the three columns:

```
H e l
l o ,
  w o
r l d
!
```

You're given the column order 1, 3, 2, so first you take the letters from the first column, followed by the third and then the second column:

```
Hl r!l,odeowl
```

That is your secret code.

## Input

You will receive three lines of input. The first will be a positive integer indicating how many columns you should use in your grid. The second line will be the order that your columns should be used in. And the third line will contain the message you need to transform into your secret code. For the example given above, the input would be:

```
3
1 3 2
Hello, world!
```

## Output

As output, you will give the secret code generated from the original message:

```
Hl r!l,odeowl
```

## Constraints

- There will never be more than 1000 columns.
- Each column will be included in the column orders in the second line of input.
- The message to be encoded will be at least one character long, and can contain letters, spaces, and punctuation.

## Examples

### Input 0

```
4
4 3 2 1
I am not a robot.
```

### Output 0

```
mtrtao o nabI  o.
```

### Input 1

```
2
1 2
Life is good.
```

### Output 1

```
Lf sgo.iei od
```
