#!/usr/bin/python3

import fileinput

nPlayers = 0
nMarbles = 0

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

for line in fileinput.input():
    line = line.rstrip()
    [nPlayers, nMarbles] = [int(x) for x in line.split()]


scores = [0]*nPlayers
startingNode = Node(0)
startingNode.left = startingNode
startingNode.right = startingNode
current = startingNode
currentPlayer = 0

for i in range(1, nMarbles+1):
    if i % 23 == 0:
        scores[currentPlayer] += i
        for step in range(7):
            current = current.left
        scores[currentPlayer] += current.value
        current.left.right = current.right
        current.right.left = current.left
        current = current.right
    else:
        newNode = Node(i)
        newNode.left = current.right
        newNode.right = current.right.right
        newNode.left.right = newNode
        newNode.right.left = newNode
        current = newNode
    currentPlayer += 1
    if currentPlayer == nPlayers:
        currentPlayer = 0

for score in scores:
    print(score)

print()
print(max(scores))
