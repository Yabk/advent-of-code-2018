#!/usr/bin/python3

import fileinput


guard = {}
currentGuard = None
previousTime = 0
asleep = False
for line in fileinput.input():
    line = line.rstrip()

    split = line.split()
    if split[2] == 'Guard':
        if asleep:
            asleep = False
            for i in range(previousTime, 60):
                guard[currentGuard][i] += 1
        currentGuard = split[3][1:]
        if currentGuard not in guard:
            guard[currentGuard] = [0]*60
    elif split[2] == 'falls':
        asleep = True
        previousTime = int(split[1][3:5])
    elif split[2] == 'wakes':
        asleep = False
        currentTime = int(split[1][3:5])
        for i in range(previousTime, currentTime):
            guard[currentGuard][i] += 1


bestGuard = 0
bestSleepTime = 0
bestMinute = 0
for grd, sleepTimes in guard.items():
    current = 0
    currentBestMinute = 0
    currentBestMinuteValue = 0
    for i in range(len(sleepTimes)):
        current += sleepTimes[i]
        if sleepTimes[i] > currentBestMinuteValue:
            currentBestMinuteValue = sleepTimes[i]
            currentBestMinute = i
    if current > bestSleepTime:
        bestSleepTime = current
        bestGuard = grd
        bestMinute = currentBestMinute

print(bestGuard)
print(bestMinute)
print(bestGuard*bestMinute)
