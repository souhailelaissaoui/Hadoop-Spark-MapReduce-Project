#!/usr/bin/python
import sys
#input comes from STDIN (standard input)
currentline = ""
currentdistance = float('inf')
currentneighbours = "EMPTY"
currentColor = "WHITE"
currentPath = ""
firstone = True
for line in sys.stdin:
    line = line.strip()
    val = line.split("\t")
    words = val[1].split("/")
    key = val[0]
    if words[0] != 'EMPTY':
        words[0] = eval(words[0]) 
    words[1] = float(words[1])
    if key != currentline:
        if not firstone:
            toprint = "/".join([str(currentneighbours), str(currentdistance), currentColor, currentPath])
            print '%s\t%s' % (currentline, toprint)
            currentline = key
            currentdistance = words[1]
            currentneighbours = words[0]
            currentColor = words[2]
            currentPath = words[3]
        else:
            currentline = key
            currentdistance = words[1]
            currentneighbours = words[0]
            currentColor = words[2]
            currentPath = words[3]
            firstone = False
    if currentdistance > words[1]:
        currentdistance = words[1]
        currentPath = words[3]
    if words[0] != 'EMPTY':
        currentneighbours = words[0]
    if words[2] == "BLACK":
        currentColor = words[2]
    if words[2] == "GRAY":
        if currentColor == "WHITE":
            currentColor = words[2]

toprint = "/".join([str(currentneighbours), str(currentdistance), currentColor, currentPath])
print '%s\t%s' % (currentline, toprint)
