with open("S5.in") as file:
	inpu = file.read().strip().split('\n')

cases = int(inpu.pop(0))

for i in range(cases):
	t = inpu.pop(0).split()
	npins = int(t[0])
	balls = int(t[1])
	width = int(t[2])
	pins = []
	for n in range(npins):
		pins.append(int(inpu.pop(0)))

	maxScores = [0 for i in range(width-1)]
	for x in range(width-1, npins):
		maxScores.append(0)
		for y in range(width):
			maxScores[-1] += pins[x-y]

	maxx = 0
	while balls > 0:
		balls -= 1
		m = max(maxScores)
		maxx += max(maxScores)
		g = maxScores.index(m)
		if g >= width:
			for s in range(width):
				pins[g-s] = 0
		else:
			for s in range(i):
				pins[s] = 0
		pins[g] = 0
		maxScores = [0 for i in range(width-1)]
		for x in range(width-1, npins):
			maxScores.append(0)
			for y in range(width):
				maxScores[-1] += pins[x-y]

	print(maxx)


# 2	8	5	1	9	6	9	3	2
# 	10	13	13	13	15	15	15	15
# 			16	23	28	28	28	28

# 2	8	5	1	9	6	9	3	2 
# 	10	13	6	10	15	15	12	5


# 1	10	99	99	10	1
# 	11	109	198	109	11