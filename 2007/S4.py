with open("S4.in") as file:
	inpu = file.read().strip().split('\n')[:-1]

# SLOW RECURSIVE:

# n = int(inpu[0])

# pf = {}
# for i in inpu[1:]:
# 	x = i.split();
# 	if int(x[1]) not in pf.keys():
# 		pf[int(x[1])] = [int(x[0])]
# 	else:
# 		pf[int(x[1])].append(int(x[0]))

# def pathsTo(p):
# 	if p == 1:
# 		return 1
# 	else:
# 		su = 0
# 		for i in pf[p]:
# 			su += pathsTo(i)
# 		return su

# print(pathsTo(n))


# FAST GOOD:

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