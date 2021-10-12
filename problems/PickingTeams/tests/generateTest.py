# Generates a large, random test
import random
from os.path import exists

NUM_STUDENTS = 25
NUM_LINES = 10000
PERCENT_COMMANDS = .75

testNumber = input('Test number: ')
inFilename = f'{testNumber}.in'
outFilename = f'{testNumber}.out'
if exists(inFilename):
    print(f'File {inFilename} already exists')
    exit(0)


def intToName(num, first=True):
    if not first and num == 0:
        return ''
    return chr(num % 26 + 97) + intToName(num // 26, False)


names = list()

print("Generating names")
for i in range(NUM_STUDENTS):
    names.append(intToName(i))


print("Creating test file")
with open(inFilename, 'w') as f:
    print(NUM_LINES, file=f)
    for i in range(NUM_LINES):
        A = random.choice(names)
        B = A
        while A == B:
            B = random.choice(names)
        print(f'{"+" if random.random() < PERCENT_COMMANDS else "?"} {A} {B}',
              file=f)

print("Finished")
