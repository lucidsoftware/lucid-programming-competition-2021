# The Green Squiggly Line

English grammar is difficult.
Even the best writers will make mistakes, which is why grammar checking tools are so useful.
Many grammar checking programs exist, and today, we will be discovering what goes into one of these checkers.

Input will consist of one or more lines containing a single sentence.
This sentence may, or may not contain grammatical errors according to the grammar rules listed below.

Enforce the following grammar rules:

1. Each sentence must start with a capital letter and end with a single period. No other periods should appear in the sentence.
2. Commas must come immediately after a word, and they must be followed by one space and then another word.
3. Multiple spaces in a row are not allowed. Each space must be singular.

By "word", we simply mean any collection of alphabetical characters.
"Proposition" and "gfhdbsf" are both words, but "hello,world" is not.

Each sentence is assigned a number, starting with 1 for the first sentence.
For each line that has improper grammar, return an ordered list of line numbers separated by spaces, or "No Problems" if no errors exist.

## Constraints
* Each file will contain at least one line of input
* There will be no more than 100 lines of input
* A line will contain a maximum of 100,000 characters

## Examples

### Input 1
```
Lucidchart is the intelligent diagramming application.
```

### Output 1
```
No Problems
```

### Input 2
```
Hello, World.
Hello, World
hello, World.
Hello,World.
Hello  World.
```

### Output 2
```
2 3 4 5
```





