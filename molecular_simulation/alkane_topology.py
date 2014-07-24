#!/usr/bin/env python

"""Tool to generate angle and dihedral information for linear alkane chains."""

__author__ = "Pierre de Buyl"
__version__ = "0.1.1"
print "This is %s %s by %s" % (__file__, __version__, __author__)

import sys

if len(sys.argv)<2:
    print "Usage: %s nc" % __file__
    print "       where nc is the number of C atoms"

import numpy as np
import networkx as nx

