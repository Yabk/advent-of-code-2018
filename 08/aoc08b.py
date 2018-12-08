#!/usr/bin/python3

import fileinput

nums = []

for line in fileinput.input():
    line = line.rstrip()
    nums = [int(x) for x in line.split(' ')]

class node():
    def __init__(self, numChildren, numMeta):
        self.numChildren = numChildren
        self.leftChildren = numChildren
        self.numMeta = numMeta
        self.children = []
        self.meta = []

    def addChild(self, child):
        self.children.append(child)

    def addMeta(self, m):
        self.meta.append(m)

    def getValue(self):
        if not self.children:
            return sum(self.meta)
        else:
            value = 0
            for childIndex in self.meta:
                if childIndex == 0:
                    continue
                try:
                    childValue = self.children[childIndex-1].getValue()
                    value += childValue
                except IndexError:
                    pass
            return value

root = node(nums.pop(0), nums.pop(0))
q = [root]
while q:
    if q[-1].leftChildren == 0:
        currentNode = q.pop()
        for i in range(currentNode.numMeta):
            currentNode.addMeta(nums.pop(0))
    else:
        q[-1].leftChildren -= 1
        newNode = node(nums.pop(0), nums.pop(0))
        q[-1].addChild(newNode)
        q.append(newNode)

print(root.getValue())
