#!/usr/bin/python3

import csv
from sys import argv

TOPOLOGY_FILE = argv[1]

with open(TOPOLOGY_FILE, newline='') as topology:
	fileReader = csv.DictReader(topology)

	nodes = []
	rows = []
	for row in fileReader:
		rows.append(row)
		for (key, value) in row.items():
			# print(key, value)
			if key == '':
				nodes.append(value)
				
	i = 0

	connections = {}
	edges = {}
	for row in rows:
		for (key, value) in row.items():
			if key == '':
				node = value
			else:
				
				edges[key] = value


		connections[node] = edges
		
		edges = {}

# for route in routes:
# 	print(f'{route[SOURCE]} -> {route[DESTINATION]} = {route[DISTANCE]}')
source_node = input("Please, provide the source node: ")
if(source_node not in nodes):
	print(f'{source_node} is not a valid node.')
	print(f'Choose from the following: {nodes}')
	exit()
print(f"Shortest path tree for node {source_node}:")

			
untested = connections
distances = {source_node:connections[source_node][source_node]}
untested = nodes
untested.remove(source_node)

print(untested)

print(f"CONNECTIONS: {connections[source_node]}")
# N_prime = {source_node}

# for node in untested:
# 	if()
