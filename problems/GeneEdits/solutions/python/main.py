import random
import time

GENES = ['A','T','C','G']

def randomGene(length = 1):
    out = []
    for _ in range(length):
        out.append(random.choice(GENES))
    return ''.join(out)

class Edit:
    def __init__(self, idx, diff=0):
        self.idx = idx
        # diff is string ? "insert this string at idx" : "remove the indicated number of characters starting at idx"
        self.diff = diff

    def __repr__(self):
        return '{} {}'.format(self.idx, self.diff)


def doEdits(gene, edits):
    out = '' # we will only ever append to this string, so there is no inefficiency
    currIdx = 0
    extra = 0
    for edit in edits:
        # move currIdx up, grab more of the original gene
        out += gene[currIdx:edit.idx-extra] # gene is never manipulated, only read from
        currIdx = edit.idx - extra # account for changes already made to the gene
        if isinstance(edit.diff, str):
            extra += len(edit.diff)
            out += edit.diff
        else:
            extra -= edit.diff
            currIdx += edit.diff
    out += gene[currIdx:]
    return out

def doEditsNaive(gene, edits):
    for edit in edits:
        if isinstance(edit.diff, str):
            gene = gene[0:edit.idx] + edit.diff + gene[edit.idx:]
        else:
            gene = gene[0:edit.idx] + gene[edit.idx + edit.diff:]
    return gene

def main():
    gene = input()
    numEdits = int(input())
    edits = []
    for _ in range(numEdits):
        idx, diff = input().split(' ')
        if diff.isnumeric():
            diff = int(diff)
        edits.append(Edit(int(idx), diff))
    now = time.time()
    best = doEdits(gene, edits)
    then = time.time()
    # print('Fast: {} ms'.format(then - now))
    now = time.time()
    naive = doEditsNaive(gene, edits)
    then = time.time()
    # print('Naive: {} ms'.format(then - now))
    # print("Matched? {}".format(best == naive))
    if best != naive:
        raise Exception("you failed")
    print(best)

if __name__ == '__main__':
    main()
