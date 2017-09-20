#!/usr/bin/env python

# Calculates piezoelectric coefficient from taking the difference between two XYZ files.
# Usage: xyz2d33.py xyz-file1 xyz-file2

import sys

if len(sys.argv) != 3:
	print("Usage: xyz2d33.py xyz-file1 xyz-file2")
	sys.exit(1)


print(sys.argv[0])

f_xyz1 = sys.argv[1]
print(f_xyz1)

f_xyz2 = sys.argv[2]
print(f_xyz2)


def read_XYZ(filename):
	f = open(filename, "r")
	NAtom = int(f.readline())
	Comment = f.readline()
	XYZ = []
	for line in f:
		Tokens = line.split()
		XYZ.append(Tokens)
	f.close()
	return (NAtom, XYZ)


NAtom1, XYZ1 = read_XYZ(f_xyz1)
print(XYZ1)

NAtom2, XYZ2 = read_XYZ(f_xyz2)
print(XYZ2)

if NAtom1 != NAtom2:
	print("NAtom1 = %d  NAtom2 = %d  => mismatch!" % (NAtom1, NAtom2))
	sys.exit(1)

for iAtom in range(NAtom1):
	for jAtom in range(iAtom+1, NAtom1):
		
