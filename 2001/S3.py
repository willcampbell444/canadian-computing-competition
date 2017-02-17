import sys
from collections import deque

alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Graph():
	def __init__(self, num_v):
		self.V = num_v
		self.nodes = [[] for _ in range(num_v)]

	def addEdge(self, a, b):
		self.nodes[a].append(b)
		self.nodes[b].append(a)

	def adjacent(self, a):
		return iter(self.nodes[a])

inp = sys.stdin.readlines()
inp.pop()

g = Graph(26)

for x in inp:
	g.addEdge(alph.find(x[0]), alph.find(x[1]))

class BFS():
	def __init__(self, graph, start):
		self.marked = [False for _ in range(26)]
		self.path_to = [-1 for _ in range(26)] # stores the previous node in the path
		self.start = start
		queue = deque()
		queue.append(start)
		self.marked[start] = True

		while queue:
			x = queue.popleft()
			for i in graph.adjacent(x):
				if not self.marked[i]:
					self.marked[i] = True
					self.path_to[i] = x
					queue.append(i)
	# get the path from the starting point to node x69
	def getPath(self, x):
		stuff = [x]
		while x != self.start and x != -1:
			x = self.path_to[x]
			stuff.append(x)
		stuff.reverse()
		return stuff

# checks if there is a path from A to B without the edge from node n1 to n2
# uses BFS
def pathWithout(graph, n1, n2):
	marked = [False for _ in range(26)]
	path_to = [-1 for _ in range(26)]
	queue = deque()
	queue.append(0)
	marked[0] = True

	while queue:
		x = queue.popleft()
		for i in graph.adjacent(x):
			if not ((x == n1 and i == n2) or (x == n2 and i == n1)):
				if i == 1:
					return True
				if not marked[i]:
					marked[i] = True
					path_to[i] = x
					queue.append(i)
	return False

b = BFS(g, 0)
path = b.getPath(1) # shortest path from A to B
count = 0
# go through each edge on the path
for n in range(len(path)-1):
	# if you can not get from A to B with the edge removed, print the edge
	if not pathWithout(g, path[n], path[n+1]):
		count += 1
		print(alph[path[n]]+alph[path[n+1]])

print("There are", count, "disconnecting roads.")