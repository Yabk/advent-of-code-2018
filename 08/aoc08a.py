#!/usr/bin/python3

import fileinput

nums = []

for line in fileinput.input():
    line = line.rstrip()
    nums = [int(x) for x in line.split(' ')]

print(nums)

sum = 0
qChildren = [nums.pop(0)]
qMeta = [nums.pop(0)]
while qChildren:
    if qChildren[-1] == 0:
        qChildren.pop()
        metaN = qMeta.pop()
        for i in range(metaN):
            sum += nums.pop(0)
    else:
        qChildren[-1] -= 1
        qChildren.append(nums.pop(0))
        qMeta.append(nums.pop(0))

print(sum)
