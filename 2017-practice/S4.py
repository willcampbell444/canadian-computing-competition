import sys, heapq

inp = sys.stdin.readlines()

numPens = int(inp.pop(0))

class Edge():
	def __init__(self, _from, to, weight):
		self.edgeTo = to
		self.edgeFrom = _from
		self.weight = weight
	def __lt__(self, other):
		return self.weight < other.weight

class Graph():
	def __init__(self, num_v):
		self.V = num_v
		self.nodes = [[] for _ in range(num_v)]
	def addEdge(self, a, b, weight):
		self.nodes[a].append(Edge(a, b, weight))
		self.nodes[b].append(Edge(b, a, weight))
	def adj(self, node):
		return iter(self.nodes[node])

def MST_Weight(graph, out=False):
	touched = [False for _ in range(graph.V)]
	V = graph.V
	edges = []

	heap = []

	touched[0] = out
	for e in graph.adj(1):
		if not touched [e.edgeTo]:
			heapq.heappush(heap, (e.weight, e))
	touched[1] = True

	while heap:
		_, edge = heapq.heappop(heap)

		if not touched[edge.edgeTo]:
			for e in graph.adj(edge.edgeTo):
				if not touched[e.edgeTo]:
					heapq.heappush(heap, (e.weight, e))
			touched[edge.edgeTo] = True
			edges.append(edge)
	for i in touched:
		if i == False:
			return 99999999
	total = 0
	for e in edges:
		total += e.weight
	return total

graph = Graph(numPens+1)
walls = {}

for l in range(len(inp)):
	line = [int(i) for i in inp[l].split()]
	numEdge = line[0]
	corners = line[1:numEdge+1]
	weights = line[numEdge+1:]
	for i in range(-1, numEdge-1):
		c1 = min(corners[i], corners[i+1])
		c2 = max(corners[i], corners[i+1])
		if (c1, c2) in walls:
			x = walls[(c1, c2)]
			del walls[(c1, c2)]
			graph.addEdge(x[1], l+1, x[0])
		else:
			walls[(c1, c2)] = (weights[i], l+1)

for x in walls.values():
	graph.addEdge(0, x[1], x[0])

print(min(MST_Weight(graph, out=False), MST_Weight(graph, out=True)))