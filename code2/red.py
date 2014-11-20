#!/usr/bin/python

import sys

wordCount = 0
oldKey = None
nodes = []

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey = data_mapped[0]

    if oldKey and oldKey != thisKey:
        nodes.sort()
        print oldKey, "\t", wordCount, "\t", '[%s]' % ', '.join(map(str, nodes))
        oldKey = thisKey;
        wordCount = 0
        nodes = []

    oldKey = thisKey
    wordCount += 1
    nodes.append(data_mapped[1])

if oldKey != None:
    nodes.sort()
    print oldKey, "\t", wordCount, "\t", '[%s]' % ', '.join(map(str, nodes))

