#!/usr/bin/python3

import csv
import pprint
from sys import argv
import itertools

pp = pprint.PrettyPrinter(indent=4)

TOPOLOGY_FILE = argv[1]

with open(TOPOLOGY_FILE, newline="") as topology:
    fileReader = csv.DictReader(topology)

    nodes = []
    rows = []
    for row in fileReader:
        rows.append(row)
        for (key, value) in list(row.items()):
            # print(key, value)
            if key == "":
                nodes.append(value)
            else:
                row[key] = int(row[key])
                

    connections = {}
    axis = {}


    for row in rows:
        for (key, value) in row.items():
            if key == "":
                node = value
            else:
                axis[key] = value
        connections[node] = axis
        axis = {}


edges_temp = []
for i in connections:
    for j in connections[i]:
        if connections[i][j] != 9999 and connections[i][j] != 0:
            edges_temp.append(sorted([i, j]))

edges_temp.sort()    
edges = list(edges_temp for edges_temp,_ in itertools.groupby(edges_temp))

for i in range(len(edges)):
    edges[i].append(connections[edges[i][0]][edges[i][1]])




def bellmanford(source, node_list, edge_weights):
    distance = {}
    predecessor = {}
    for vertex in node_list:
        distance[vertex] = 9999
    distance[source] = 0

    for _ in range(len(node_list) - 1):
        for u,v,w in edge_weights:
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
    
    print(distance)

print(edges)
bellmanford('u', nodes, edges)
