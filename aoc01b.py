#!/usr/bin/python3

import fileinput

if __name__ == '__main__':
    current = 0
    list = []
    for line in fileinput.input():
        list.append(int(line))

    set = {current}

    index = 0
    while True:
        if index >= len(list):
            index = 0

        current += list[index]
        if current in set:
            break
        set.add(current)

        index += 1

    print(current)
#-112892
