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

	edges = [('source' ,'destination', 'length')]
	for row in rows:

		for j, (key, value) in enumerate(row.items()):
			if (key != ''):
				edges.append((nodes[i], key, int(value)))
				# print(f'{nodes[i]} connects to {key} with {value}')
		i += 1

SOURCE = 0

DESTINATION = 1

DISTANCE = 2


# for route in routes:
# 	print(f'{route[SOURCE]} -> {route[DESTINATION]} = {route[DISTANCE]}')
source_node = input("Please, provide the source node: ")
print(f"Shortest path tree for node {source_node}:")

# N_prime is current path

possible_paths = []
distance = 0
i = 0
untested = nodes
tested = ""
distance = 9999
current_node = ""
for edge in edges:
	if (edge[SOURCE] == source_node):
		print(edge)
	
# 	if edge[SOURCE] == source_node:
# 		current_node = source_node


		
# 	if current_node not in tested:
# 		if 


# 		# Not connected
# 		#if route[DISTANCE] != '9999':


# 		# 	if(route[DESTINATION] == destination_node):
# 		# 		distance += route[DISTANCE]

# 		# 	if(current_node == destination_node):
# 		# 		possible_paths.append((current_node, destination_node, distance))
# 		# 	while(current_node != destination_node):
				

# print(f"Costs of the least-cost paths for node {source_node}")
# print(possible_paths)



			
