with open("S4.in") as file:
	inpu = file.read().strip().split('\n')[:-1]

length = int(inpu.pop(0))
nodes = [[] for i in range(length)]
pp = [0 for i in range(length)]
pp[0] = 1

slides = [[int(j) for j in i.split()] for i in inpu]

for x in slides:
	nodes[x[0]-1].append(x[1]-1)

total = 0
while sum(pp[:-1]) > 0:
	np = [0 for i in range(length)]
	for i in range(length):
		if pp[i] > 0:
			for j in nodes[i]:
				np[j] += pp[i]
	total += np[-1]
	pp = np

print(total)