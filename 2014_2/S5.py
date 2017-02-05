import sys

class Digraph():
	def __init__(self, vertecies):
		self._nodes = [[] for i in range(vertecies)]

	def add_vertex(self):
		self._nodes.append(set())

	def add_edge(self, edgefrom, edgeto):
		self._nodes[edgefrom].append(Edge(edgefrom, edgeto, 1))

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

class UndirectedGraph(Digraph):
	def add_edge(self, edgefrom, edgeto):
		self._nodes[edgefrom].add(Edge(edgefrom, edgeto, 1))
		self._nodes[edgeto].add(Edge(edgeto, edgefrom, 1))

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

	def __hash__(self):
		return self._from*self._to + self._from*self.weight + self.weight

	def __repr__(self):
		return "<Edge: "+str(self._from)+" -> "+str(self._to)+", weight="+str(self._weight)+">"

class WeightedDigraph(Digraph):
	def add_edge(self, edgefrom, edgeto, weight):
		self._nodes[edgefrom].append(Edge(edgefrom, edgeto, weight))

class WeightedUndirectedGraph(WeightedDigraph):
	def add_edge(self, v1, v2, weight):
		self._nodes[v1].append(Edge(v1, v2, weight))
		self._nodes[v2].append(Edge(v2, v1, weight))

x = sys.stdin.read().strip().split('\n')
x.pop(0)
points = [[int(j) for j in i.split()] for i in x]
points.append([0, 0])
edges = []

for p1 in range(len(points)):
	for p2 in range(p1+1, len(points)):
		edges.append((p1, p2, (points[p1][0]-points[p2][0])**2 + (points[p1][1]-points[p2][1])**2))

edges.sort(key = lambda x: x[2])

fromm = {}

for e in edges:
	if e[0] not in fromm:
		fromm[e[0]] = 0
	if e[1] not in fromm:
		fromm[e[1]] = 0

	new0 = -1
	new1 = -1

	if e[1] in fromm and fromm[e[1]]+1 > fromm[e[0]] and e[1] != len(points)-1:
		new0 = fromm[e[1]]+1

	if e[0] in fromm and fromm[e[0]]+1 > fromm[e[1]] and e[0] != len(points)-1:
		new1 = fromm[e[0]]+1

	if new0 != -1:
		fromm[e[0]] = new0
	if new1 != -1:
		fromm[e[1]] = new1

print(fromm[len(points)-1])