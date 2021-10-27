letters = input()

d = dict()

d['a'] = 0
d['p'] = 0
d['l'] = 0
d['e'] = 0



for c in letters:
    if c not in d:
        d[c] = 0
    d[c] += 1


print(min([d['a'], d['l'], d['e'], d['p'] // 2]))


