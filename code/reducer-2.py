#!/usr/bin/python

import sys

maxSales = 0
txnSales = 0
oldKey = None
oldTxn = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisTxn, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        if thisSale > maxSales:
            maxSales = thisSale
        print oldKey, "\t", maxSales 
        oldKey = thisKey;
        oldTxn = None
        maxSales = 0
        thisSale = 0

    oldKey = thisKey

    if oldTxn and oldTxn != thisTxn:
        if thisSale > maxSales:
            maxSales = thisSale
        thisSale = 0

if oldKey != None:
    print oldKey, "\t", maxSales

