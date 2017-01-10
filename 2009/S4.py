import sys
# 1, 

with open("S4.in") as file:
	inpu = file.read().strip().split('\n')

# inpu = sys.stdin.read().strip().split('\n')

# cities = int(inpu[0])
routes = [[int(j) for j in i.split()] for i in inpu[2:int(inpu[1])+2]]
retailers = [[int(j) for j in i.split()] for i in inpu[int(inpu[1])+3:-1]]
destination = int(inpu[-1])

expiditions = [[destination, 0]]
done = []
# visited = []
while expiditions:
	newExpiditions = []
	if len(done) > 0:
		winning = min(done)
		for e in expiditions:
			if e[1] < winning:
				for r in routes:
					if e[0] == r[0]:
						newExpiditions.append([r[1], e[1]+r[2]])
						routes.remove(r)
					elif e[0] == r[1]:
						newExpiditions.append([r[0], e[1]+r[2]])
						routes.remove(r)
	else:
		for e in expiditions:
			for r in routes:
				if e[0] == r[0]:
					newExpiditions.append([r[1], e[1]+r[2]])
					routes.remove(r)
				elif e[0] == r[1]:
					newExpiditions.append([r[0], e[1]+r[2]])
					routes.remove(r)
	expiditions = newExpiditions
	for e in expiditions:
		for i in retailers:
			if e[0] == i[0]:
				done.append(e[1]+i[1])

print(min(done))