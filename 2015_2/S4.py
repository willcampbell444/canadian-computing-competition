import sys
import heapq
import itertools

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

class UndirectedGraph(Digraph):
	def add_edge(self, edgefrom, edgeto):
		self._nodes[edgefrom].add(Edge(edgefrom, edgeto, 1))
		self._nodes[edgeto].add(Edge(edgeto, edgefrom, 1))

class Edge():
	def __init__(self, edgefrom, edgeto, weight, thickness):
		self._from = edgefrom
		self._to = edgeto
		self._weight = weight
		self._thickness = thickness

	def getFrom(self):
		return self._from

	def getTo(self):
		return self._to

	def getWeight(self):
		return self._weight

	def getThickness(self):
		return self._thickness

	def __lt__(self, other):
		return self._weight < other.getWeight()

	def __repr__(self):
		return "<Edge: "+str(self._from)+" -> "+str(self._to)+", weight="+str(self._weight)+">"

class WeightedDigraph(Digraph):
	def add_edge(self, edgefrom, edgeto, weight, thickness):
		self._nodes[edgefrom].add(Edge(edgefrom, edgeto, weight, thickness))

class WeightedUndirectedGraph(WeightedDigraph):
	def add_edge(self, v1, v2, weight, thickness):
		self._nodes[v1].add(Edge(v1, v2, weight, thickness))
		self._nodes[v2].add(Edge(v2, v1, weight, thickness))

class PriorityQueue():
	def __init__(self):
		self._heap = []
		self._item_to_entry = {}
		self._counter = itertools.count()

	def insert(self, item, priority):
		if item in self._item_to_entry:
			self.remove(item)
		count = next(self._counter)
		entry = [priority, count, item]
		self._item_to_entry[item] = entry
		heapq.heappush(self._heap, entry)

	def popmin(self):
		while self._heap:
			priority, _, task = heapq.heappop(self._heap)
			if task is not None:
				del self._item_to_entry[task]
				return task
		raise KeyError("Pop from empty queue")

	def remove(self, item):
		entry = self._item_to_entry.pop(item)
		entry[-1] = None

	def __bool__(self):
		return bool(self._heap)

	def __repr__(self):
		return repr(self._heap)

x = sys.stdin.read().strip().split('\n')
z = x.pop(0).split()
strength = int(z[0])
num_vert = int(z[1])

z = x.pop().split()
start = int(z[0])-1
end = int(z[1])-1

islands = WeightedUndirectedGraph(num_vert)

for r in x:
	r = [int(i) for i in r.split()]
	islands.add_edge(r[0]-1, r[1]-1, r[2], r[3])


pq = PriorityQueue()
pq.insert((start, strength, 0), 0)
win = False
time = 100000000
while pq:
	x = pq.popmin()
	if x[0] == end:
		win = True
		if x[2] < time:
			time = x[2]
		break
	for i in islands.adjacent(x[0]):
		if x[1] - i.getThickness() > 0:
			pq.insert((i.getTo(), x[1] - i.getThickness(), x[2] + i.getWeight()), x[2] + i.getWeight())
if win:
	print(time)
else:
	print(-1)