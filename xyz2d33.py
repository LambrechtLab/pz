#!/usr/bin/env python

# Calculates piezoelectric coefficient from taking the difference between two XYZ files.

import sys
import math

if len(sys.argv) != 4:
	### USAGE ###
	print("Usage: xyz2d33.py xyz-file1 xyz-file2 Field1")
	print("")
	print("xyz-file1 is the geometry _after_ in the field.")
	print("xyz-file2 is the geometry _without_ the field.")
	print("Field1 is the field strength.")
	print("Note: Field2 is assumed to always be zero.")
	###
	sys.exit(1)


print(sys.argv[0])

f_xyz1 = sys.argv[1]
print(f_xyz1)

f_xyz2 = sys.argv[2]
print(f_xyz2)

F1 = float(sys.argv[3])
F2 = 0

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

def distance(iXYZ, jXYZ):
	
	x1 = float(iXYZ[1])
	y1 = float(iXYZ[2])
	z1 = float(iXYZ[3])
	x2 = float(jXYZ[1])
	y2 = float(jXYZ[2])
	z2 = float(jXYZ[3])
	R = math.sqrt( (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2 )

	return R

deltaF = F1 - F2


d33 = 0
i = 0
j = 0
for iAtom in range(NAtom1):
	for jAtom in range(iAtom+1, NAtom1):
		Rij_mol1 = distance(XYZ1[iAtom], XYZ1[jAtom])		
		Rij_mol2 = distance(XYZ2[iAtom], XYZ2[jAtom])		
		deltaR = Rij_mol1 - Rij_mol2
		d = (100/Rij_mol2) * deltaR / deltaF # (pm/V)
		if d > d33:
			d33 = d
			i = iAtom
			j = jAtom
		print("d(%d,%d) = %.2f  pm/V" % (iAtom, jAtom, d))

print("D33 = %.2f  pm/V     (atom pair: %d - %d)" % (d33, i, j))
