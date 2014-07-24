#!/usr/bin/env python

"""Tool to generate angle and dihedral information for linear alkane chains."""

__author__ = "Pierre de Buyl"
__version__ = "0.1.2"
print "This is %s %s by %s" % (__file__, __version__, __author__)

import sys

if len(sys.argv)<2:
    print "Usage: %s nc" % __file__
    print "       where nc is the number of C atoms"
    exit()

import numpy as np
import networkx as nx

nc=int(sys.argv[1])

# Create graph with backbone C atoms
G = nx.Graph()
G.add_edges_from( [(i, i+1) for i in range(1, nc)] )

# Add 4-deg H atoms for each C
H_idx=nc+1
for n_idx in G.nodes():
    deg = nx.degree(G, n_idx)
    print n_idx, deg
    for i in range(4-deg):
        G.add_edge(n_idx, H_idx)
        H_idx+=1

print G.nodes()
