#!/usr/bin/python3

import csv
from sys import argv

import copy


TOPOLOGY_FILE = argv[1]

with open(TOPOLOGY_FILE, newline='') as topology:
	fileReader = csv.DictReader(topology)

	nodes = []
	rows = []
	for row in fileReader:
		rows.append(row)
		for (key, value) in list(row.items()):
        	# print(key, value)
			if key == "":
				nodes.append(value)
			elif value == '9999':
				del row[key]
			else:
				row[key] = int(row[key])
				
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

N_prime = [source_node]
untested = copy.deepcopy(connections)
del untested[source_node][source_node]

distances = {}


# for key, entry in connections.items():
# 	print(key, entry)

for key, entry in connections[source_node].items():
	distances[key] = entry

while(N_prime != nodes):
	minimum = 9999
	for key, value in untested[source_node].items():
		if key in N_prime:
			pass
		elif value < minimum:
			minimum = value
			minimum_node = key

	N_prime.append(minimum_node)
	del untested[source_node][minimum_node]
	N_prime.sort()

	distances[node] = min(distances[node], distances[minimum_node] + connections[minimum_node][node])


		

print(distances)
