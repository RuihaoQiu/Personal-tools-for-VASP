#!/usr/bin/env python

# This program is to plot band structure without projecting to orbits
# Input file -- OUTCAR and PROCAR

#__author__ = Ruihao QIU
#__email__ = qiuruihao@gmail.com

# Import operator
# Plot function for Python
import matplotlib.pyplot as plt
import numpy as np
from numpy import array as npa

# define a find_str() function
# notice, the str should be the only one in the whole text.
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
#print Ef,nk,nb

# Get band structure data from PROCAR
band = [line.split() for line in open ('PROCAR', 'r')]
eng = npa([float(band[j][4]) for j, ln in enumerate(band) if "energy" in ln])
data = np.reshape(eng, (nk,nb)).T-Ef
#print data

x = np.arange(1,nk+1)
for i in range(nb):
	plt.plot(x,data[i],color=(0., 0., 1.))
plt.show()

# Just a simple plot. feel free to improve the plot by revising the plt.plot
