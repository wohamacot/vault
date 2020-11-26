from __future__ import print_function
from collections import defaultdict
from sys import exit, argv

if len(argv) < 3:
    print("ArgumentError")
    print("usage: flipout.py <inputfile.out> <outputfile.out>")
    exit()

inputfile = argv[1]
outputfile = argv[2]

with open(inputfile) as f:
    data = defaultdict(list)
    for line in f:
        key = line[:line.find(':')].strip()
        if line.startswith(" MD step:"):
            data[key].append(line.split()[2])
        else:
            data[key].append(line[line.find(':')+2:].split()[2])

with open(outputfile,'w') as f:
    for row in zip(*data.values()):
        f.write('\t'.join(row) + '\n')
    print("{} was created".format(outputfile))    

