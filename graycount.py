import sys

inp = sys.argv[1]
r = open(inp, "r")
lines = r.readlines()
nb = 0
for line in lines:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    val = line.split("\t")
    words = val[1].split("/")
    
    if words[2] == 'GRAY':
        nb += 1
print(nb)