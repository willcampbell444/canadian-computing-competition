

with open("S5.in") as file:
	inpu = file.read().strip().split('\n')

tests = [[int(i) for i in j.split()] for j in inpu[1:]]

for test in tests:
	pos = [test]
	c = 0
	done = False
	while True:
		c += 1
		newpos = []
		react = False
		for i in pos:
			if i[0] > 1 and i[1] > 0 and i[3] > 1:
				newpos.append([i[0]-2, i[1]-1, i[2], i[3]-1])
				react = True
			if i[0] > 0 and i[1] > 0 and i[2] > 0 and i[3] > 0:
				newpos.append([i[0]-1, i[1]-1, i[2]-1, i[3]-1])
				react = True
			if i[2] > 1 and i[3] > 0:
				newpos.append([i[0], i[1], i[2]-2, i[3]-1])
				react = True
			if i[1] > 2:
				newpos.append([i[0], i[1]-3, i[2], i[3]])
				react = True
			if i[0] > 0 and i[3] > 0:
				newpos.append([i[0]-1, i[1], i[2], i[3]-1])
				react = True
		if not react:
			break
		pos = newpos
		# print(pos)
	print(c%2)