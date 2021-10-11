
import sys

def encodeMessage():
    numColumns = int(input())
    columnOrder = input().split(" ")
    message = input()
    secretCode = ""
    stringList = []

    for column in range(numColumns):
        stringList.append("")

    for i in range(len(message)):
        stringList[i%numColumns] += message[i]

    for columnNumber in columnOrder:
        secretCode += stringList[int(columnNumber)-1]

    print(secretCode)

encodeMessage()