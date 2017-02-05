import heapq
import itertools
import sys

class PriorityQueue():
	def __init__(self):
		self._heap = []
		self._counter = itertools.count()

	def insert(self, item, priority):
		count = next(self._counter)
		entry = [priority, count, item]
		heapq.heappush(self._heap, entry)

	def popmin(self):
		if self._heap:
			priority, _, task = heapq.heappop(self._heap)
			return task
		raise KeyError("Pop from empty queue")

	def __bool__(self):
		return bool(self._heap)

	def __repr__(self):
		return repr(self._heap)

inp = sys.stdin.read().strip().split('\n')
inp.pop(0)
threshold = int(inp.pop(0))

vertical = PriorityQueue()
for i in inp:
	i = [int(j) for j in i.split()]
	vertical.insert((i[1], i[3], i[4], i[0]), i[0])
	vertical.insert((i[1], i[3], -i[4], i[2]), i[2])

horizontal = []
area = 0
pos = 0

while vertical:
	lenAbove = 0
	t = 0
	ppos = 0
	for p in horizontal:
		if t >= threshold:
			lenAbove += p[0]-ppos
		ppos = p[0]
		t += p[1]

	entry = vertical.popmin()

	area += lenAbove*(entry[3]-pos)
	pos = entry[3]

	if entry[2] > 0:
		horizontal.append((entry[0], entry[2]))
		horizontal.append((entry[1],-entry[2]))
		horizontal.sort(key = lambda x: x[0])
	else:
		horizontal.remove((entry[0],-entry[2]))
		horizontal.remove((entry[1], entry[2]))

print(area)