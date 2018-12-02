#!/usr/bin/python3

import fileinput

if __name__ == '__main__':
    current = 0
    for line in fileinput.input():
        current += int(line)
        print(current)

    print(current)
#-112892
