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

### Explanation

First, Alice claims Bob. Let's call them team A. Next, Charlie claims David. Let's call them team B. The answer to the query `? Alice Charlie` is no, because Alice is on team A and Charlie on team B. Bob and Alice are both on team A, so we return yes for the second query.

Next, Bob claims Charlie. Charlie comes to team A, and brings all those he brought to team B. In this case, that is David. Now, all four students are on team A. Note that David is now considered stolen. If there were to be more queries, he would never leave team A. Also note that Charlie is not considered stolen yet, because this is the first time he has been claimed by another team.

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

### Explanation

The first three commands of this input match the first three commands of Input 0, meaning Alice, Bob, Charlie, and David are all on team A, and David is considered stolen.

Next, Emily claims Alice. Alice has not been stolen (or even claimed) yet, so she moves to Emily's team (team C). Alice brought Bob to team A, so he comes with her. Bob brought both Charlie and David to team A. Charlie has not been stolen yet, so he comes to team C with Bob. However, David has already been stolen, and so he remains on team A. Now, team A consists of just David, team B is empty, and team C consists of Alice, Bob, Charlie, and Emily. Since team B is empty, we do not count it in the final team count. To clarify, at the end of the input, Bob, Charlie, and David have all been stolen once, and are thus locked into their respective teams. Alice has been claimed once, so she may move teams one more time. Emily has not been claimed nor stolen yet.
