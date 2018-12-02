#!/usr/bin/python3

import fileinput

two = 0
tree = 0
for line in fileinput.input():
    letters = {}
    for i in range (len(line)-1):
        if line[i] not in letters:
            letters[line[i]] = 1
        else:
            letters[line[i]] += 1

    two_found = False
    tree_found = False
    for (letter, times) in letters.items():
        if times == 2 and not two_found:
            two_found = True
            two += 1
        if times == 3 and not tree_found:
            tree_found = True
            tree += 1

print(two*tree)
