#!/usr/bin/python
import sys
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    val = line.split("\t")
    words = val[1].split("/")
    key = val[0]
    words[1] = float(words[1])
    if words[2] == 'GRAY':
        toprint = "/".join([words[0], str(words[1]), "BLACK", words[3]])
        print '%s\t%s' % (key, toprint)
        words[0] = eval(words[0])
        for i in words[0]:
            toprint = "/".join(["EMPTY", str(words[1] + 1), "GRAY", str(words[3])+ str(key)+ ","])
            print '%s\t%s' % (i, toprint)
    else:
        toprint = "/".join([words[0], str(words[1]), words[2], words[3]])
        print '%s\t%s' % (key, toprint)

