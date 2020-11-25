# flipout.py inputfile.out outputfile.out

import pandas as pd
from sys import exit, argv
from itertools import chain

if len(argv) < 3:
    print("ArgumentError")
    print("usage: flipout.py <inputfile.out> <outputfile.out>")
    exit()

inputfile = argv[1]
outputfile = argv[2]
_width = 6
steps = []
pressure = []
potentialE = []
MD_Kinetic = []
Total_MD_Energy = []
MD_Temperature = []
titles = []
with open(inputfile) as f:
    for line in f:
        titles.append(line.split(":")[0].strip())
        if line.startswith(" MD s"):
            steps.append(" ".join(line.split())[9:])
        elif line.startswith(" Pressure"):
            pressure.append(" ".join(line.split()).split(" ")[3])
        elif line.startswith(" Potential"):
            potentialE.append(" ".join(line.split()).split(" ")[4])
        elif line.startswith(" MD Kinetic"):
            MD_Kinetic.append(" ".join(line.split()).split(" ")[5])
        elif line.startswith(" Total"):
            Total_MD_Energy.append(" ".join(line.split()).split(" ")[5])
        elif line.startswith(" MD T"):
            MD_Temperature.append(" ".join(line.split()).split(" ")[4])



dic = dict(
    chain(
        {titles[0]: steps}.items(),
        {titles[1]: pressure}.items(),
        {titles[2]: potentialE}.items(),
        {titles[3]: MD_Kinetic}.items(),
        {titles[4]: Total_MD_Energy}.items(),
        {titles[5]: MD_Temperature}.items(),
    )
)

df = pd.DataFrame.from_dict(dic)
df[df.columns] = df[df.columns].astype(str)

tempdf = {}
for i, eCol in enumerate(df):
    tempdf[i] = pd.Series(df[eCol]).str.pad(width=_width)

pd.concat(tempdf, axis=1).to_csv(
    outputfile, sep="\t", index=False, header=False, mode="w"
)

print("{} was created".format(outputfile))
