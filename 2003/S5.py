import sys, heapq

class Edge():
	def __init__(self, _to, _from, _weight):
		self.weight = _weight
		self.edgeFrom = _from
		self.edgeTo = _to
	def __lt__(self, other):
		return self.weight > other.weight

class Graph():
	def __init__(self, v):
		self.v = v
		self.nodes = [[] for _ in range(v)]
	def addEdge(self, _from, to, weight):
		self.nodes[_from].append(Edge(to, _from, weight))
		self.nodes[to].append(Edge(_from, to, weight))

class ThickestPath():
	def __init__(self, graph, start):
		self.thicks = [0 for _ in range(graph.v)]
		self.marked = [False for _ in range(graph.v)]
		heap = [(-9999999, Edge(0, -1, 0))]

		while heap:
			priority, edge = heapq.heappop(heap)
			if not self.marked[edge.edgeTo]:
				self.marked[edge.edgeTo] = True
				self.thicks[edge.edgeTo] = -priority
				for e in graph.nodes[edge.edgeTo]:
					if not self.marked[e.edgeTo]:
						heapq.heappush(heap, (max(-e.weight, priority), e))

inp = sys.stdin.read().strip().split('\n')

x = inp.pop(0).split()
num_cities = int(x[0])
num_roads = int(x[1])

graph = Graph(num_cities)

for x in inp[:num_roads]:
	x = x.split()
	graph.addEdge(int(x[0])-1, int(x[1])-1, int(x[2]))

destinations = [int(i)-1 for i in inp[num_roads:]]

# graphTwo = Graph(len(destinations))
# for d in range(len(destinations)):
# 	thicc = ThickestPath(graph, d)
# 	for f in range(d+1, len(destinations)):
# 		graphTwo.addEdge(d, f, thicc.thicks[f])

thicc = ThickestPath(graph, 0)
print(min(thicc.thicks[x] for x in destinations))
