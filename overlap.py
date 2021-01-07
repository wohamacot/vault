from sys import exit, argv

if len(argv) < 4:
    print("ArgumentError")
    print("usage: overlap.py <inputfile> <values> <outputfile>")
    exit()


_input = []
values = []

with open(argv[2]) as f:
    for line in f.readlines():
        values.append(line.strip()[:6])

with open(argv[1]) as f:    
    for line in f.readlines():
        _input.append(line.strip())

with open(argv[3], "w") as f:
    for i in _input:
        for j in values:
            if i.startswith(j):
                f.write(i + "\n")
