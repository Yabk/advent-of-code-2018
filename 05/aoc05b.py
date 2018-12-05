#!/usr/bin/python3

import fileinput

chars = []
for line in fileinput.input():
    line = line.rstrip()
    print(line)

    chars = list(line)

print(chars)

possible = set()
for char in chars:
    if char.lower() not in possible:
        possible.add(char.lower())

best = 21321123
print(possible)
for char in possible:
    i = 0
    working = chars[:]
    while i < len(working):
        if working[i].lower() == char:
            working.pop(i)
        else:
            i += 1

    i = 0
    while i < len(working)-1:
        if (working[i].lower() == working[i+1].lower()) and (working[i] != working[i+1]):
            working.pop(i)
            working.pop(i)
            if i > 0:
                i -= 1
        else:
            i += 1
    if len(working) < best:
        best = len(working)


print(best)
