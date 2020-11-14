#!/usr/bin/python3

####################################################
# Peyton Page and Vivian Carr
# CSC 450 - Link-State & Distance-Vector Routing
# Implements Link-State Routing
# using Dijkstra's Algorithm
#
# Implements Distance-Vector Routing
# using the Bellman-Ford Equation
#
# Sources:
# CSC450 Network Layer P3 Notes & Recorded Lecture
####################################################


import csv
from sys import argv
import copy
import pprint
import itertools

DEBUG = False
# Read file from command line
TOPOLOGY_FILE = argv[1]

def dijkstras(TOPOLOGY_FILE, DEBUG):
	# open file
	with open(TOPOLOGY_FILE, newline='') as topology:
		fileReader = csv.DictReader(topology)

		# get list of nodes
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
					
		# form dictionary of edges
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

	# get user input
	source_node = input("Please, provide the source node: ")

	# ensure input is in graph
	if(source_node not in nodes):
		print(f'{source_node} is not a valid node.')
		print(f'Choose from the following: {nodes}')
		exit()


	# Initialization
	# N' = {u}
	N_prime = [source_node]
	untested = copy.deepcopy(connections)
	del untested[source_node][source_node]

	# Make copy of connections for calculating distances
	distances = copy.deepcopy(connections[source_node])

	for key, entry in connections[source_node].items():
		distances[key] = entry

	# Create dictionary for forming shortest path trees
	path = {}
	for node in nodes:
		path[node] = source_node + node


	# Repeat until all nodes in N'
	while(N_prime != nodes):
		# Set minimum to the max for finding min
		minimum = 9999
		# find w not in N' (untested) such that D(w) is a minimum
		for key, value in untested[source_node].items():
			if key in N_prime:
				pass
			elif value <= minimum:
				minimum = value
				minimum_node = key


		# add w to N'
		N_prime.append(minimum_node)
		
		# remove w from untested
		del untested[source_node][minimum_node]
		
		# Sort N_prime for comparison to nodes
		N_prime.sort()

		# update D(v) for all v adjacent to w and not in N'
		for node in untested:
			temp = copy.deepcopy(distances[node])
			distances[node] = min(distances[node], distances[minimum_node] + connections[minimum_node][node])
			# If distance is updated through new path, update the path for that node
			if(distances[node] != temp):
				path[node] = path[minimum_node] + node

	# Create output string of shortest paths
	print(f"Shortest path tree for node {source_node}:")
	del path[source_node]
	shortest_path = ''	
	for key, value in path.items():
		shortest_path += f"{value}, "
	shortest_path = shortest_path.rstrip(', ')
	print(shortest_path)

	print(f"Costs of the least-cost paths for node {source_node}:")
	# Create output string of cost of least-cost paths
	least_cost = ""
	for key, value in distances.items():
		least_cost += f"{key}:{value}"
		least_cost += ', '
	least_cost = least_cost.rstrip(', ')	
	# output cost of least_cost paths
	print(least_cost)

	if(DEBUG):
		for source, entry in connections.items():
			for destination, distance in entry.items():
				print(f'{source} --> {destination} = {distance}')
			print()

def bellmanford(TOPOLOGY_FILE):
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



if __name__ == "__main__":
	dijkstras(TOPOLOGY_FILE, DEBUG)
	bellmanford(TOPOLOGY_FILE)
