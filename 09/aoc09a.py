#!/usr/bin/python3

import fileinput

nPlayers = 0
nMarbles = 0

for line in fileinput.input():
    line = line.rstrip()
    [nPlayers, nMarbles] = [int(x) for x in line.split()]


scores = [0]*nPlayers
game = [0]
current = 0
currentPlayer = 0

for i in range(1, nMarbles+1):
    if i % 23 == 0:
        scores[currentPlayer] += i
        current -= 7
        current %= len(game)
        scores[currentPlayer] += game.pop(current)
        current %= len(game)
    else:
        current = current + 2
        current %= len(game)
        game.insert(current, i)
    currentPlayer += 1
    if currentPlayer == nPlayers:
        currentPlayer = 0

for score in scores:
    print(score)

print()
print(max(scores))
