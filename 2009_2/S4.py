import sys, heapq

class Edge():
	def __init__(self, fr, to, weight):
		self.fr = fr
		self.to = to
		self.weight = weight

class Graph():
	def __init__(self, V):
		self.prices = [None for _ in range(V)]
		self.V = V
		self.nodes = [[] for _ in range(V)]

	def setPrice(self, node, price):
		self.prices[node] = price

	def addEdge(self, a, b, weight):
		self.nodes[a].append(Edge(a, b, weight))
		self.nodes[b].append(Edge(b, a, weight))

	def adj(self, node):
		return iter(self.nodes[node])

inp = sys.stdin.readlines()
num_cities = int(inp.pop(0))
num_routes = int(inp.pop(0))
destination = int(inp.pop())-1

cities = Graph(num_cities)

for route in inp[:num_routes]:
	r = route.split()
	cities.addEdge(int(r[0])-1, int(r[1])-1, int(r[2]))

for store in inp[num_routes+1:]:
	r = store.split()
	cities.setPrice(int(r[0])-1, int(r[1]))

heap = [(0, destination)]
marked = [False for _ in range(num_cities)]
lowest = 999999

while heap:
	curr_dist, curr_node = heapq.heappop(heap)
	if curr_dist > lowest:
		break
	if not marked[curr_node]:
		marked[curr_node] = True
		if cities.prices[curr_node] and lowest > curr_dist + cities.prices[curr_node]:
			lowest = curr_dist + cities.prices[curr_node]
		for node in cities.adj(curr_node):
			if not marked[node.to]:
				heapq.heappush(heap, (curr_dist+node.weight, node.to))

print(lowest)