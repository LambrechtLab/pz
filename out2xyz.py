#!/usr/bin/env python

# Converts MOPAC output file to XYZ file.
# Usage: out2xyz.py out-file xyz-file

import sys

if len(sys.argv) != 3:
	print("Usage: out2xyz.py out-file xyz-file")
	sys.exit(1)


print(sys.argv[0])

f_out = sys.argv[1]
print(f_out)

f_xyz = sys.argv[2]
print(f_xyz)


# Reads the Cartesian coordinates from the MOPAC output file and stores them in XYZ (a list of lists :)

f = open(f_out, "r")
XYZ = []
for line in f:
	#print(line)
	if "                             CARTESIAN COORDINATES" in line:
		#print(line)
		empty = f.next()
		for line in f:
			if not line.strip():
				break
			#print(line)
			Tokens = line.split() 
			#print(Tokens)
			XYZ.append(Tokens)
f.close()
print(XYZ)


f = open(f_xyz, "w")
NAtom = len(XYZ)
f.write("%d\n" % NAtom)
f.write("\n")
for line in XYZ:
	print(line)
	f.write("%s   %10.6f   %10.6f   %10.6f\n" % (line[1], float(line[2]), float(line[3]), float(line[4])))

f.close()
