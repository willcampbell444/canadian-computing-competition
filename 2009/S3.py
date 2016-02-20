# PERFECT


with open("S3.in") as file:
	inpu = file.read().strip().split('\n')

peeple = [
	[5],
	[5],
	[14, 4, 3, 5],
	[2, 5, 4],
	[2, 3, 5],
	[0, 1, 2, 3, 4, 6],
	[5, 7],
	[6, 8],
	[7, 9, 11],
	[8, 10],
	[9, 11],
	[8, 10, 12],
	[11, 13, 14],
	[12],
	[2, 12],
	[16, 17],
	[15, 17],
	[15, 16]
]

people = {}

for i in range(len(peeple)):
	people[i] = peeple[i]

tmp = []
m = []
for i in inpu:
	if i in "idnfsq":
		tmp.append(m)
		m = [i]
	else:
		m.append(i)

for i in tmp[1:]:

	if i[0] == 'i':
		x = int(i[1])-1
		y = int(i[2])-1

		if x not in people.keys():
			people[x] = []
		if y not in people.keys():
			people[y] = []
		if x not in people[y]:
			people[x].append(y)
			people[y].append(x)

	if i[0] == 'd':
		x = int(i[1])-1
		y = int(i[2])-1

		people[x].remove(y)
		people[y].remove(x)

	if i[0] == 'n':
		x = int(i[1])-1

		print(len(people[x]))

	if i[0] == 'f':
		x = int(i[1])-1

		fofs = []
		for d in people[x]:
			for n in people[d]:
				if n != x and n not in fofs and n not in people[x]:
					fofs.append(n)
		print(len(fofs))

	if i[0] == 's':
		x = int(i[1])-1
		y = int(i[2])-1

		count = 0
		ppl = [x]
		visited = []
		while len(ppl) != 0 and y not in ppl:
			count += 1
			visited.extend(ppl)
			newppl = []

			for h in ppl:
				for j in people[h]:
					if j not in visited and j not in newppl:
						newppl.append(j)
			ppl = newppl
		if len(ppl):
			print(count)
		else:
			print("Not connected")

	if i[0] == 'q':
		break

