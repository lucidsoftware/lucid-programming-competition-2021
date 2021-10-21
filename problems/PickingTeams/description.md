# Picking Teams

A group of students is choosing teams for a snowball fight after school. However, they are quite unorganized.

The students begin calling out the names of other students they want on their team. When a student's name is called out, they join the team of the caller. If the caller did not have a team before, the two are now considered a new team.

To make it more interesting, students may also claim students from other teams. So, if Alice claims Bob, they are now on a team together. Charlie can then claim Bob and move Bob to his team. Now, Alice is on a team by herself and Charlie and Bob are on another team. However, to keep this process from continuing forever, they decide each student may only be claimed a maximum of 2 times. So, to continue the example above, David cannot claim Bob, since he has already been claimed twice (once by Alice and once by Charlie). Bob is now considered "unclaimable." Note that in this example, Bob is the only student to have been claimed at all thus far. Even though Alice and Charlie both claimed Bob and thus formed new teams, neither of them were claimed by another student, so they may each sitll be claimed 2 more times.

Finally, when a student is moved to a new team, they take all the students with them that they brought to their current team. Being moved to a new team in this manner (being moved to a new team with one's "parent") also counts as being claimed, and counts toward each student's 2 claims. Thus, when moving to a new team, a student only brings their "children" that have not been double-claimed, and any children they do bring are considered double-claimed after the move. If the students they bring also have "children," the moving process continues with them. If a child is unclaimable, the process does not continue with their children.

To try to bring some order to the chaos, the students also ask if another student is already on their team.

After processing all commands and queries, any students not yet on a team form teams of size 1. So, if Emily does not yet have a team at the end of input, she forms a team that consists of just Emily (and presumably feels a bit left out). Every student's name will appear in the input at least once.

No student will claim themself. If a student tries to claim a student already on their team, do nothing.

## Input

Input will begin with a non-negative integer N <= 100000, representing the number of lines that follow. Each of the following N lines will be either a command or a query. Commands are in the form `+ A B`, meaning student A adds student B to their team. Queries are in the form `? A B`, meaning "Are students A and B on the same team?" Again, every student's name will appear in either a command or query at least once. Every name will be unique and consist only of lowercase and uppercase letters [a-zA-Z].

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

Next, Bob claims Charlie. Charlie comes to team A, and brings all those he brought to team B. In this case, that is David. Now, all four students are on team A. Note that David has been claimed twice now. If there were to be more commands, he would never leave team A. Also note that Charlie is not considered double-claimed yet, because this is the first time he has been claimed by another team. Bob has been claimed once, and Alice has been claimed 0 times.

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

The first three commands of this input match the first three commands of Input 0, meaning Alice, Bob, Charlie, and David are all on team A. Alice has been claimed 0 times, Bob and Charlie once each, and David twice.

Next, Emily claims Alice. Alice has been claimed less than 2 times, so she moves to Emily's team (team C). Alice brought Bob to team A, so he comes with her (and Bob becomes double-claimed). Bob brought both Charlie and David to team A. Charlie is not double-claimed yet, so he comes to team C with Bob. However, David has already been claimed twice, and so he remains on team A. Now, team A consists of just David, team B is empty, and team C consists of Alice, Bob, Charlie, and Emily. Since team B is empty, we do not count it in the final team count. To clarify, at the end of the input, Bob, Charlie, and David have all been double-claimed, and are thus locked into their respective teams. Alice has been claimed once, so she may move teams one more time. Emily has not been claimed at all yet.
