# Picking Teams

A group of students is choosing teams for a snowball fight after school. However, they are quite unorganized.

Each student starts as his or her own team. Each student then takes turns calling out the name of someone to add to their team (in no particular order). There are no team captains, meaning any member of the team may add another teammate. There may also be any number of teams. Additionally, each student may be stolen from another team exactly 1 time. When a student is stolen, they take all the students they are responsible for adding to the team with them (the students they added, the students those students added, etc). When a student is stolen, all those they bring to the new team are considered stolen as well and may not be stolen again. When a student is being stolen, if they have descendants that have been stolen before, those descendants (and their descendants) stay. To limit the confusion, the students may also ask if another teammate is already on their team.

No student will claim themself. If a student tries to claim a student already on their team, do nothing.

## Input

Input will begin with a non-negative integer N <= 100000, representing the number of lines that follow. Each of the following N lines will be either a command or a query. Commands are in the form `+ A B`, meaning student A adds student B to his or her team. Queries are in the form `? A B`, meaning "Are students A and B on the same team?" You may assume that every student's name will appear in either a command or query at least once. Every name will be unique and consist only of lowercase and uppercase letters [a-zA-Z].

## Output

Do not output anything for commands, even if a student tries to steal an already stolen student. For each query, output 'yes' or 'no'. After processing all commands and queries, output the total number of teams.

## Examples

### Input 0
```
6
+ Alice Bob
+ Charlie David
? Alice Charlie
? Bob Alice
+ Bob Charlie
? Alice David
```

### Output 0
```
no
yes
yes
1
```

### Input 1
```
7
+ Alice Bob
+ Charlie David
+ Bob Charlie
? Alice Charlie
+ Emily Alice
? Emily Bob
? Emily David
```

### Output 1
```
yes
yes
no
2
```
