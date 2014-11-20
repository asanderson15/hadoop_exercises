#!/usr/bin/python

import sys
import re

regex = re.compile('([^ ]*) ([^ ]*) ([^ ]*) \[([^]]*)\] "([^"]*)" ([^ ]*) ([^ ]*)')

for line in sys.stdin:
    m = re.match(regex, line)
    if not m:
        continue
    host, ignore, user, date, request, status, size = m.groups()

    try:
        method, file, protocol = request.split(" ")
        fileOnly = file
    except:
        fileOnly = "ERROR"
        pass

    #fileOnly = request

    try:
        if fileOnly.startswith("http://www.the-associates.co.uk"):
            fileEnd = fileOnly[31:]
        elif fileOnly.startswith("https://www.the-associates.co.uk"):
            fileEnd = fileOnly[32:]
        else:
            fileEnd = fileOnly
    except:
        fileEnd = fileOnly
        pass


    print "{0}".format(fileEnd)
