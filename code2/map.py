#!/usr/bin/python

import sys
import csv
import re


reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

regex = re.compile('[\.\;\,\s\!\"\?\[\]\:\;\(\)\<\>\#\$\=\-/]+')

for line in reader:
    node = line[0]
    try:
        words = list(regex.split(line[4]))
        words = [x.lower() for x in words]
    except:
        pass

    for word in words:
        print "{0}\t{1}".format(word, node)
