#!/usr/bin/python3

import fileinput


def print_out(box_a, box_b):
    for i in range(len(box_a)):
        if box_a[i] == box_b[i]:
            print(box_a[i], end='')
    print()
    print(box_a)
    print(box_b)

boxes = []
for line in fileinput.input():
    boxes.append(line.rstrip())

good = False
for i in range(len(boxes)-1):
    if not good:
        for j in range(i+1, len(boxes)):
            diff = 0
            good = True
            for k in range(len(boxes[i])):
                if boxes[i][k] != boxes[j][k]:
                    diff +=1
                    if diff > 1:
                        good = False
                        break
            if good:
                print_out(boxes[i], boxes[j])
                break
