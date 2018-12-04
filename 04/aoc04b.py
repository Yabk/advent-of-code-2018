#!/usr/bin/python3

import fileinput


guard = {}
currentGuard = None
previousTime = 0
asleep = False

entries = []
for line in fileinput.input():
    line = line.rstrip()
    split = line.split()

    date = int(''.join(split[0][1:].split('-')))
    hour = int(split[1][0:2])
    minute = int(split[1][3:5])
    entry = []

    if split[2] == 'Guard':
        entry = [date, hour, minute, 'newGuard', int(split[3][1:])]
    elif split[2] == 'wakes':
        entry = [date, hour, minute, 'wakesUp']
    elif split[2] == 'falls':
        entry = [date, hour, minute, 'fallsAsleep']
    else:
        print('error01')

    inserted = False
    for i in range(len(entries)):
        if entry[0] < entries[i][0]:
            entries.insert(i, entry)
            inserted = True
            break
        if entry[0] == entries[i][0]:
            if entry[1] < entries[i][1]:
                entries.insert(i, entry)
                inserted = True
                break
            if entry[1] == entries[i][1]:
                if entry[2] < entries[i][2]:
                    entries.insert(i, entry)
                    inserted = True
                    break
                if entry[2] == entries[i][2]:
                    print('error02')
    if not inserted:
        entries.append(entry)

# print(len(entries))
# for entry in entries:
#     for element in entry:
#         print(element, end= ' ')
#     print()

asleep = False
previousTime = 0
currentGuard = 0
for entry in entries:
    if entry[3] == 'newGuard':
        #print()
        #print('new guard: '+split[3][1:])
        if asleep:
            #print('previus was asleep from '+str(previousTime))
            asleep = False
            for i in range(previousTime, 60):
                guard[currentGuard][i] += 1
        currentGuard = entry[4]
        if currentGuard not in guard:
            #print('adding new guard')
            guard[currentGuard] = [0]*60
    elif entry[3] == 'fallsAsleep':
        if not asleep:
            asleep = True
            previousTime = int(entry[2])
            #print('guard '+currentGuard+' falls asleep minute '+str(previousTime))
    elif entry[3] == 'wakesUp':
        if asleep:
            asleep = False
            currentTime = int(entry[2])
            #print('guard '+currentGuard+' wakes up minute '+str(currentTime))
            for i in range(previousTime, currentTime):
                guard[currentGuard][i] += 1


bestGuard = 0
bestMinute = 0
bestMinuteValue = 0

for grd, sleepTimes in guard.items():
    for i in range(len(sleepTimes)):
        if sleepTimes[i] > bestMinuteValue:
            bestGuard = grd
            bestMinute = i
            bestMinuteValue = sleepTimes[i]

print(bestGuard)
print(bestMinute)
print(int(bestGuard)*bestMinute)

#21555
#82324
