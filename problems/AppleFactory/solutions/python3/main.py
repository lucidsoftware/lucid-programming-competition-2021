import sys

def fruitBasketSolution():
    letters=input()

    a = 0
    p = 0
    l = 0
    e = 0
    
    for letter in letters:
        if letter == 'a':
            a+=1
        if letter == 'p':
            p+=1
        if letter == 'l':
            l+=1
        if letter == 'e':
            e+=1
            
    print(min(a, p//2, l, e))

fruitBasketSolution()

