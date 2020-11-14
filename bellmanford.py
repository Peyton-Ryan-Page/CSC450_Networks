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


edges = []
for i in connections:
    for j in connections[i]:
        if connections[i][j] != 9999 and connections[i][j] != 0:
            edges.append([i, j, connections[i][j]])

for each in nodes:
    distance = {}

    for vertex in nodes:
        distance[vertex] = 9999
    distance[each] = 0

    for _ in range(len(nodes) - 1):
        for u, v, w in edges:
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    print("Distance vector for node", each + ":", *list(distance.values()), sep=" ")
