import sys

# with open("S2.in") as file:
	# inpu = file.read().strip().split('\n')

inpu = sys.stdin.read().strip().split('\n')

rooms = int(inpu.pop(0))

maze = []

for i in range(rooms):
	maze.append([int(j)-1 for j in inpu.pop(0).split()[1:]])

starts = [int(i)-1 for i in inpu[1:]]

def walk(r, d, t):
	if r == t:
		return 1
	i = maze[r].index(d)
	if i == 0:
		return 1+walk(maze[r][-1], r, t)
	else:
		return 1+walk(maze[r][i-1], r, t)

for start in starts:
	m = 0
	for i in maze[start]:
		# w = walk(i, start, start)
		w = 0
		x = i
		xx = start
		bb = False
		while True:
			if x == start:
				break
			p = maze[x].index(xx)
			if p == 0:
				xx = x
				x = maze[x][-1]
				w += 1
			else:
				xx = x
				x = maze[x][p-1]
				w += 1
		if w > m:
			m = w
	print(m+1)