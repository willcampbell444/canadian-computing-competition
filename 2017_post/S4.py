import sys, heapq

inp = sys.stdin.readlines()

x = inp.pop(0).split()
num_buildings = int(x[0])

class Edge():
	def __init__(self, _from, to, weight):
		self.edgeFrom = _from
		self.edgeTo = to
		self.weight = weight
	def __lt__(self, other):
		return self.weight < other.weight
	def __hash__(self):
		return self.edgeFrom*23 + self.edgeTo*17 + self.weight
	def __eq__(self, other):
		return (self.edgeTo == other.edgeTo) and (self.edgeFrom == other.edgeFrom) and (self.weight == other.weight)

class Graph():
	def __init__(self, V):
		self.V = V
		self.nodes = [[] for _ in range(V)]
	def addEdge(self, a, b, weight):
		self.nodes[a].append(Edge(a, b, weight))
		self.nodes[b].append(Edge(b, a, weight))
	def adj(self, node):
		return iter(self.nodes[node])

initial = set()
graph = Graph(num_buildings)

for l in range(len(inp)):
	line = [int(i) for i in inp[l].split()]
	if l < num_buildings-1:
		graph.addEdge(int(line[0])-1, int(line[1])-1, int(line[2])-0.1)
	else:
		graph.addEdge(int(line[0])-1, int(line[1])-1, int(line[2]))

def MST(graph):
	touched = [False for _ in range(graph.V)]
	edges = []

	heap = []

	for e in graph.adj(0):
		heapq.heappush(heap, e)
	touched[0] = True

	while heap:
		edge = heapq.heappop(heap)
		if not touched[edge.edgeTo]:
			for e in graph.adj(edge.edgeTo):
				if not touched[e.edgeTo]:
					heapq.heappush(heap, e)
			touched[edge.edgeTo] = True
			edges.append(edge)

	return edges

edgesRequired = MST(graph)

days = 0
for e in edgesRequired:
	if e.weight % 1 == 0:
		days += 1

print(days)