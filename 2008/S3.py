# 6:15 - , 7:10, 15/15

with open("S3.in") as file:
	inpu = file.read().strip().split('\n')[1:]

maps = []

i = 0
mapp = []
while i < len(inpu):
	if inpu[i][0] in "-+*|":
		mapp.append(inpu[i])
	elif len(mapp) > 0:
		maps.append(mapp)
		mapp = []
	i += 1
maps.append(mapp)

for m in maps:
	bpeople = [[0 for j in i] for i in m]
	people = [i[:] for i in bpeople]
	people[0][0] = 1
	mc = len(people)*len(people[0])
	count = 1
	while True:
		if people[-1][-1]:
			print(count)
			break
		elif m[-1][-1] == '*':
			print(-1)
			break
		count += 1
		newPeople = [i[:] for i in bpeople]
		for x in range(len(people)):
			for y in range(len(people[x])):
				if people[x][y]:
					type = m[x][y]
					if type == '+':
						if x > 0:
							newPeople[x-1][y] = 1
						if x < len(people)-1:
							newPeople[x+1][y] = 1
						if y > 0:
							newPeople[x][y-1] = 1
						if y < len(people[x])-1:
							newPeople[x][y+1] = 1
					elif type == '|':
						if x > 0:
							newPeople[x-1][y] = 1
						if x < len(people)-1:
							newPeople[x+1][y] = 1
					elif type == '-':
						if y > 0:
							newPeople[x][y-1] = 1
						if y < len(people[x])-1:
							newPeople[x][y+1] = 1
		people = newPeople
		if people[-1][-1]:
			print(count)
			break
		elif count > mc:
			print(-1)
			break

