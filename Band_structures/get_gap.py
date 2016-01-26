#!/usr/bin/env python

# This program is to get the band gap from band structure.
# Two files are required -- PROCAR and OUTCAR.

#__author__ = Ruihao QIU
#__email__ = qiuruihao@gmail.com

# Import operator
# Plot function for Python
import matplotlib.pyplot as plt
import numpy as np
from numpy import array as npa
from numpy import concatenate as npc

# define a find_str() function
# notice, the str should be the only one in the text whole
def find_str(str):
	line = 0
	for ln in whole:
		line = line + 1
		if str in ln:
			return(line-1)
			break


# Get fermi level from OUTCAR
out = open ('OUTCAR', 'r')
whole = [line.split() for line in out]
out.close()
lf = find_str("E-fermi")
Ef = float(whole[lf][2])
lk = find_str("NKPTS")
nk = int(whole[lk][3])
nb = int(whole[lk][-1])
#print Ef, nk,nb

# Get band structure data from PROCAR
band = [line.split() for line in open ('PROCAR', 'r')]
eng = npa([float(band[j][4]) for j, ln in enumerate(band) if "energy" in ln])
data = np.reshape(eng, (nk,nb))-Ef
#print data

"""
# Test if it is a metal
for i in range(nb):
	if all(data[i][j] >= 0 for j in range(nk)) or all(data[i][j] <= 0 for j in range(nk)):
		continue
	else:
		print 'band %s crosses fermi level' %(i+1) 
"""	

c = []
v = []
for i in range(nk):
	for j in range(nb):
		if data[i][j] > 0:
			c = c + [data[i][j]]
			v = v + [data[i][j-1]]
			break

m_dir = min(np.subtract(npa(c),npa(v)))
m_indir = min(npa(c))-max(npa(v))

if m_indir < 0:
	print "There is no band gap!!!"
elif m_dir <= m_indir:
	print "The direct band gap is %s." % m_dir
else:
	print "The indirect band gap is %s." % m_indir
