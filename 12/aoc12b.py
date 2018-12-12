#!/usr/bin/python3

import fileinput

transitions = {}
state = []


def pad(state, indexes):
    first = state.index('#')
    for i in range(first, 3):
        indexes.insert(0, indexes[0]-1)
        state.insert(0, '.')

    countEnd = 0
    if state[-1] == '.':
        if state[-2] == '.':
            if state[-3] == '#':
                indexes.append(indexes[-1]+1)
                state.append('.')
        else:
            for i in range(2):
                indexes.append(indexes[-1]+1)
                state.append('.')
    else:
        for i in range(3):
            indexes.append(indexes[-1]+1)
            state.append('.')



i = 0
for line in fileinput.input():
    line = line.rstrip()
    if i > 1:
        split = line.split(' => ')
        transitions[split[0]] = split[1]
    if i == 0:
        state = list(line.split(': ')[1])
    i += 1

print(state)
print(transitions)

indexes = [x for x in range(len(state))]
print(indexes)

for iter in range(1, 50000000001):
    print()
    print(iter)
    print(len(state))
    pad(state, indexes)
    newState = ['.', '.']

    for pot in range(2, len(state)-2):
        current = ''.join(state[pot-2:pot+3])
        try:
            newState.append(transitions[current])
        except KeyError:
            newState.append('.')
    newState.append('.')
    newState.append('.')

    state = newState
    sum = 0
    for i in range(len(state)):
        if state[i] == '#':
            sum += indexes[i]
    print(sum)

strIndexes = [str(x) for x in indexes]
print(' '.join(strIndexes))
print(' '.join(state))

sum = 0
for i in range(len(state)):
    if state[i] == '#':
        sum += indexes[i]
print(sum)
