from sys import stdin
lines = stdin.readlines()

CAPS = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
LETTERS = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

errors = []
for i, line in enumerate(lines):
    line = line.strip('\n')
    if line == '':
        continue
    if len(line) < 2:
        errors.append(i + 1)
        continue
    if line[0] not in CAPS or line[-1] != '.' or line[-2] == '.':
        errors.append(i + 1)
        continue
    prev = '0'
    for ic, c in enumerate(line):
        if prev == ',' and c != ' ':
            errors.append(i + 1)
            break
        if prev == ' ' and c == ' ':
            errors.append(i + 1)
            break
        if c == '.' and ic < len(line) - 1:
            errors.append(i + 1)
            break
        prev = c

if len(errors) > 0:
    print(*errors)
else:
    print('No Problems')
