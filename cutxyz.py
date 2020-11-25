# cutxyz.py oldfile.xyz newfile.xyz N

from sys import exit, argv

if len(argv) < 4:
   print('ArgumentError')
   print('usage: cutxyz.py <oldfile.xyz> <newfile.xyz> <N>')
   exit()

inputfile = argv[1]
ouputfile = argv[2]
N = int(argv[3])

n_atoms = ''
data = []

with open(inputfile) as xyz:
   n_atoms = xyz.readline()
   try:
      l = xyz.read().split(n_atoms)   
      data = tuple(l[1:])
   except ValueError as e:
      print('number of atoms not found')
      exit()

with open(ouputfile,'w') as out:
   for i in data[0::N]:
      out.write(n_atoms)
      out.write(i)
   print("{} was created".format(ouputfile))
