#!/usr/bin/env python

"""Tool to generate angle and dihedral information for linear alkane chains."""

__author__ = "Pierre de Buyl"
__version__ = "0.1.6"
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
if nc==1:
    G.add_node(1)
else:
    G.add_edges_from( [(i, i+1) for i in range(1, nc)] )

for idx in G.nodes():
    G.node[idx]['species']='C'

# Add 4-deg H atoms for each C
H_idx=nc+1
for n_idx in G.nodes():
    deg = nx.degree(G, n_idx)
    print n_idx, deg
    for i in range(4-deg):
        G.add_node(H_idx)
        G.node[H_idx]['species']='H'
        G.add_edge(n_idx, H_idx)
        H_idx+=1

print G.nodes()

angles=set()
dihedrals=set()
for n_idx in G.nodes():
    neighbors = nx.neighbors(G, n_idx)
    for n in neighbors:
        next_neighbors = nx.neighbors(G, n)
        for nn in next_neighbors:
            if n_idx<nn:
                angles.add( (n_idx, n, nn) )
            elif n_idx>nn:
                angles.add( (nn, n, n_idx) )
            next_next_neighbors = nx.neighbors(G, nn)
            for nnn in next_next_neighbors:
                if (n_idx!=n and n_idx!=nn and n_idx!=nnn and
                    n!=nn and n!=nnn and nn!=nnn):
                    if n_idx<nnn:
                        dihedrals.add( (n_idx, n, nn, nnn) )
                    elif n_idx>nnn:
                        dihedrals.add( (nnn, nn, n, n_idx) )

print("Angles"), len(angles)
for angle in angles:
    print angle, map(lambda i: G.node[i]['species'], angle)

print("Dihedrals"), len(dihedrals)
for dihedral in dihedrals:
    print dihedral, map(lambda i: G.node[i]['species'], dihedral)
