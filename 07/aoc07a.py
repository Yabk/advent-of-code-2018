#!/usr/bin/python3

import fileinput

dependencies = []
canDo = set()
cantDo = set()
notDone = set()

for line in fileinput.input():
    line = line.split()
    print(line[1], line[7])

    dependencies.append((line[1], line[7]))
    if (line[1] not in cantDo):
        canDo.add(line[1])
    try:
        canDo.remove(line[7])
    except KeyError:
        pass
    cantDo.add(line[7])

    try:
        notDone.add(line[1])
    except KeyError:
        pass
    try:
        notDone.add(line[7])
    except KeyError:
        pass

print(canDo)
print(cantDo)
print(notDone)


while notDone:
    canDoList = list(canDo)
    canDoList.sort()
    current = canDoList[0]
    print(current, end='')
    canDo.remove(current)
    notDone.remove(current)
    potentialNext = set()

    i = 0
    while i < len(dependencies):
        if dependencies[i][0] == current:
            potentialNext.add(dependencies[i][1])
            dependencies.pop(i)
        else:
            i += 1

    for candidate in potentialNext:
        good = True
        for dependency in dependencies:
            if dependency[1] == candidate:
                good = False
                break
        if good:
            cantDo.remove(candidate)
            canDo.add(candidate)
print()
