from collections import deque

JUDE = "Jude"

N = int(input())
children = dict()
children[JUDE] = list()
profile = dict()
profile[JUDE] = [1, 0]
for n in range(N):
    person, boss, percentKept = input().split(' ')
    percentKept = int(percentKept) / 100
    if person not in profile:
        profile[person] = [0, 0] # percent kept, profit
    if boss not in profile:
        profile[boss] = [0, 0] # percent kept, profit
    if person not in children:
        children[person] = list()
    if boss not in children:
        children[boss] = list()
    children[boss].append(person)
    profile[person][0] = percentKept

# convert percent kept to actual percent kept
q = deque()
q.append((JUDE, 1))
while len(q) > 0:
    per, mult = q.popleft()
    for child in children[per]:
        profile[child][0] *= mult
        q.append((child, profile[child][0]))

# Add profits before distribution
M = int(input())
for m in range(M):
    person, earnings = input().split(' ')
    earnings = int(earnings)
    profile[person][1] += earnings

def getTotalRevenueAndProfitWithheld(person):
    totalRevenue = profile[person][1]
    totalProfit = 0
    for child in children[person]:
        newRevenue, newProfit = getTotalRevenueAndProfitWithheld(child)
        totalRevenue += newRevenue
        totalProfit += newProfit
    profile[person][1] = totalRevenue - ((totalRevenue * (1 - profile[person][0])) + totalProfit)
    return totalRevenue, totalProfit + profile[person][1]

# for jChild in children[JUDE]:
#     profile[JUDE][1] += getTotalRevenueAndProfitWithheld(jChild) * profile[jChild][0]
getTotalRevenueAndProfitWithheld(JUDE)
for person in sorted(profile.keys()):
    print(person, round(profile[person][1]))

