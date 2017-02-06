import sys
from collections import deque

class Digraph():
	def __init__(self, vertecies):
		self._nodes = [set() for i in range(vertecies)]

	def add_vertex(self):
		self._nodes.append(set())

	def add_edge(self, edgefrom, edgeto):
		self._nodes[edgefrom].add(Edge(edgefrom, edgeto, 1))

	def adjacent(self, vertex):
		return iter(self._nodes[vertex])

	def degree(self, vertex):
		return len(self._nodes[vertex])

	def num_vertecies(self):
		return len(self._nodes)

	def num_edges(self):
		return sum(len(edges) for edges in self._nodes)

	def __str__(self):
		return str(self._nodes)

class Edge():
	def __init__(self, edgefrom, edgeto, weight=1):
		self._from = edgefrom
		self._to = edgeto
		self._weight = weight

	def getFrom(self):
		return self._from

	def getTo(self):
		return self._to

	def getWeight(self):
		return self._weight

	def __lt__(self, other):
		return self._weight < other.getWeight()

	def __repr__(self):
		return "<Edge: "+str(self._from)+" -> "+str(self._to)+", weight="+str(self._weight)+">"

class BFS():
	def __init__(self, graph, start):
		self._distTo = [-1 for _ in range(graph.num_vertecies())]
		self._touched = [False for _ in range(graph.num_vertecies())]
		self._from = [-1 for _ in range(graph.num_vertecies())]
		self._start = start

		self._distTo[start] = 0
		self._touched[start] = True

		queue = deque()
		queue.append(start)

		while queue:
			vertex = queue.popleft()
			for v in graph.adjacent(vertex):
				if not self._touched[v.getTo()]:
					queue.append(v.getTo())
					self._distTo[v.getTo()] = self._distTo[vertex]+1
					self._touched[v.getTo()] = True
					self._from[v.getTo()] = vertex

	def isReachable(self, vertex):
		return self._touched[vertex]

	def distanceTo(self, vertex):
		return self._distTo[vertex]

	def pathTo(self, vertex):
		path = []
		pos = vertex
		while pos != self._start:
			path.append(pos)
			pos = self._from[pos]
		path.append(pos)
		path.reverse()
		return path

inp = sys.stdin.read().strip().split('\n')

z = inp.pop(0).split()
num_students = int(z[0])
num_compares = int(z[1])

z = inp.pop().split()
a = int(z[0])
b = int(z[1])

graph = Digraph(num_students)

for i in inp:
	i = i.split()

	graph.add_edge(int(i[0])-1, int(i[1])-1)

abfs = BFS(graph, a-1)
bbfs = BFS(graph, b-1)
if abfs.isReachable(b-1):
	print("yes")
elif bbfs.isReachable(a-1):
	print("false")
else:
	print("unknown")