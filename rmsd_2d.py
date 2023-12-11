import MDAnalysis as mda
from MDAnalysis.analysis import diffusionamap, align
import matplotlib.pyplot as plt 
import numpy as np 

a = ""
b = "dinamica_alinhada.dcd"

u = mda.Universe(a, b)

aligner = align.AlignTraj(u, u, select='name CA', in_memory=True).run()

matrix = diffusionamap.DistanceMatrix(u, select='name CA').run()

plt.imshow(matrix.dist_matrix, cmap='viridis',vmin=0,vmax=6)
plt.xlabel('Frame', weight='bold', fontsize=20)
plt.ylabel('Frame', weight='bold', fontsize=20)

plt.colorbar(label='RMSD')

ax.plt.gca()
ax.tick_params(axis='both', labelsize=10)

plt.title('RMSD',weight='bold')

plt.show()
#fig1.figure.savefig('figura.tif', dpi=300)
