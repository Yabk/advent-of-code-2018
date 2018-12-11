#!/usr/bin/python3

import fileinput

gridSize = 300

input = 0
for line in fileinput.input():
    input = int(line.rstrip())

def getBest(grid, cellSize):
    sumX = []
    for y in range(gridSize):
        row = []
        for x in range(gridSize-cellSize+1):
            row.append(sum(grid[y][x:(x+cellSize)]))
        sumX.append(row)

    best = -3000000
    bestCoords = (0,0)
    for y in range(gridSize-cellSize+1):
        for x in range(gridSize-cellSize+1):
            value = 0
            for i in range(cellSize):
                value += sumX[y+i][x]
            if value > best:
                best = value
                bestCoords = (x+1, y+1)

    return best, bestCoords


grid = []
for y in range(gridSize):
    rack = []
    for x in range(gridSize):
        cell = ((x+11)*(y+1) + input) * (x+11)
        rack.append(((cell // 100) % 10) - 5)
    grid.append(rack)

best = -300000000
bestSize = 0
bestCoords = (0,0)
for i in range(1, gridSize+1):
    print('currentSize: '+str(i))
    currentBest, currentCoords = getBest(grid, i)
    if currentBest > best:
        best = currentBest
        bestSize = i
        bestCoords = currentCoords

print(best)
print(bestCoords)
print(bestSize)
