#!/usr/bin/python3

import fileinput

chars = []
for line in fileinput.input():
    line = line.rstrip()
    print(line)

    chars = list(line)

print(chars)

i = 0
while i < len(chars)-1:
    if (chars[i].lower() == chars[i+1].lower()) and (chars[i] != chars[i+1]):
        chars.pop(i)
        chars.pop(i)
        mijenjao = True
        if i > 0:
            i -= 1
    else:
        i += 1

print(chars)
print(len(chars))


#35336
