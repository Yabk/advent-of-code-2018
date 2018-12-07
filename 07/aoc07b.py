#!/usr/bin/python3

import fileinput

dependencies = []
canDo = set()
cantDo = set()
notDone = set()

def printWorkers(workers, time, result):
    if len(workers) > 2:
        print("{:4}    {:1}     {:1}     {:1}    {:1}    {:1}    {}".format(time, workers[0][1],
        workers[1][1], workers[2][1], workers[3][1], workers[4][1], result))
    else:
        print("{:4}    {:1}     {:1}    {}".format(time, workers[0][1],
        workers[1][1], result))

for line in fileinput.input():
    line = line.split()

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

cost = {}
counter = 61
for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    cost[letter] = counter
    counter += 1

workers = [[0, ''], [0, ''], [0, ''], [0, ''], [0, '']]
#workers = [[0, ''], [0, '']]

time = 0
result = ''
while notDone:
    addToResult = []
    change = True
    currentStepDoneWorker = []
    while change:
        change = False
        for i in range (len(workers)):
            if i not in currentStepDoneWorker:
                if workers[i][0] == 0:
                    if workers[i][1]:
                        change = True
                        currentStepDoneWorker.append(i)
                        doneNow = workers[i][1]
                        notDone.remove(doneNow)
                        potentialNext = set()
                        addToResult.append(doneNow)

                        j = 0
                        while j < len(dependencies):
                            if dependencies[j][0] == doneNow:
                                potentialNext.add(dependencies[j][1])
                                dependencies.pop(j)
                            else:
                                j += 1

                        for candidate in potentialNext:
                            good = True
                            for dependency in dependencies:
                                if dependency[1] == candidate:
                                    good = False
                                    break
                            if good:
                                cantDo.remove(candidate)
                                canDo.add(candidate)
                    if not canDo:
                        workers[i][1] = ''
                        continue
                    canDoList = list(canDo)
                    canDoList.sort()
                    current = canDoList[0]
                    canDo.remove(current)
                    workers[i][0] = cost[current]
                    workers[i][1] = current

                if workers[i][0] > 0:
                    workers[i][0] -= 1
                    currentStepDoneWorker.append(i)

    addToResult.sort()
    result += ''.join(addToResult)
    printWorkers(workers, time, result)
    time += 1

print(result)
print(time-1)

#FDSEGPLJKNRYOAQUIMHTCVWZXB
#FSDEGPLJKNRYOQUAIMHTCVWZXB
#FSDEGPJLKNRYOQUAIHMTCVWZXB
#1001
