import sys

inp = sys.stdin.readlines()

numslides = int(inp.pop(0))
inp.pop()

class Graph():
	def __init__(self, V):
		self.nodes = [[] for _ in range(V)]
		self.V = V
	def addEdge(self, a, b):
		self.nodes[a].append(b)
	def adjacent(self, a):
		return iter(self.nodes[a])

slide = Graph(numslides)

for s in inp:
	s = [int(i)-1 for i in s.split()]
	slide.addEdge(s[1], s[0])

_numPaths = {0: 1}

def numPaths(graph, node):
	if node in _numPaths:
		return _numPaths[node]
	else:
		total = 0
		for a in graph.adjacent(node):
			total += numPaths(graph, a)
		_numPaths[node] = total
		return total

print(numPaths(slide, numslides-1))