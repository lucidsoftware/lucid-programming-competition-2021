# Gene Edits
After numerous, grotesque failed experiments, you've finally learned the secret to bending genetic code to your will. Now all you need is a system for applying your edits to a given gene sequence to bring your horrific mutants to life.

Given a sequence of genes, and a list of edits, apply the requested edits to the given gene sequence, and output the result

### Input Format
> G
> E
> (edit 1)
> (edit 2)
> ...
> (edit E)

Input will be formatted as shown above. The first line will contain a string "G" that is the original gene. The second line will contain an integer "E" followed by "E" lines of edits.

##### Edit Format
> 16 GTC
> 21 6

Edits will come in two forms: "additions" and "deletions". Every edit starts with an integer representing an index in the gene to manipulate. An addition entails inserting the following gene segment (a string) into the gene sequence at the provided index (such that the new characters are found *before* the original character at that index). A deletion entails removing the number of genes indicated by the second integer.

### Example 
#### Input:
> ACTG
> 3
> 1 GG
> 4 1
> 5 TCA
#### Output:
> AGGCGTCA

### Constraints
* Max length of G: 50,000
* Max number of edits: 15,000
* Max length of added/removed text: 10
* Edit indexes are unique
* Edits are ordered from lowest index to highest index
* Edits are applied sequentially; the index of a subsequent edit is applied to the outcome of the prior edit
* Edits will not overlap; new characters added to the sequence will not be removed by later deletions, and new characters added to the sequence will not be added in the middle of previously added substrings
