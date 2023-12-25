#!/bin/bash
import sys
import networkx as nx

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()

f = read_input()
s = f.split("\n")

g = nx.Graph()

for line in s:
    l, r = line.split(': ')
    for x in r.split():
        g.add_edge(l, x)
        g.add_edge(x, l)

g.remove_edges_from(nx.minimum_edge_cut(g))
group1, group2 = nx.connected_components(g)

print(len(group1) * len(group2))
