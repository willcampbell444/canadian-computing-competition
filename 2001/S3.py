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

	def adj(self, a):
		return iter(self.nodes[a])

inp = sys.stdin.read().strip().split()
inp.pop()

g = Graph(26)

for x in inp:
	g.addEdge(alph.find(x[0]), alph.find(x[1]))

class BFS():
	def __init__(self, graph, start):
		self.marked = [False for _ in range(26)]
		self.path_to = [-1 for _ in range(26)]
		self.start = start
		queue = deque()
		queue.append(start)
		self.marked[start] = True

		while queue:
			x = queue.popleft()
			for i in graph.adj(x):
				if not self.marked[i]:
					self.marked[i] = True
					self.path_to[i] = x
					queue.append(i)

	def getPath(self, x):
		stuff = [x]
		while x != self.start and x != -1:
			x = self.path_to[x]
			stuff.append(x)
		stuff.reverse()
		return stuff

def pathWithout(graph, a, b):
	marked = [False for _ in range(26)]
	path_to = [-1 for _ in range(26)]
	queue = deque()
	queue.append(0)
	marked[0] = True

	while queue:
		x = queue.popleft()
		for i in graph.adj(x):
			if not ((x == a and i == b) or (x == b and i == a)):
				if i == 1:
					return True
				if not marked[i]:
					marked[i] = True
					path_to[i] = x
					queue.append(i)
	return False

b = BFS(g, 0)
path = b.getPath(1)
count = 0
for n in range(len(path)-1):
	if not pathWithout(g, path[n], path[n+1]):
		count += 1
		print(alph[path[n]]+alph[path[n+1]])

print("There are", count, "disconnecting roads.")