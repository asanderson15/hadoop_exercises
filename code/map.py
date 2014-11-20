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
        fileOnly = file.split("?")[0]
    except:
        fileOnly = "ERROR"
        pass

    print "{0}".format(fileOnly)
