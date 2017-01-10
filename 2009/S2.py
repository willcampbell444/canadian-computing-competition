# Perfect

with open("S2.in") as file:
	inpu = file.read().strip().split('\n')

inpu = inpu[2:]

grid = [[bool(int(j)) for j in i.split()] for i in inpu]
grid.reverse()

possible = [grid[-1]]
for row in range(len(grid)-1):
	row = len(grid)-2-row

	newPossible = [grid[row]]
	for p in possible:
		success = True
		while success:
			success = False
			np = p[:]
			for n in range(len(p)):
				if grid[row][n] == p[n]:
					np[n] = False
				else:
					np[n] = True
			if np not in newPossible:
				newPossible.append(np)
				success = True
	possible = newPossible

print(len(possible))
