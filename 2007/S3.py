with open("S3.in") as file:
	inpu = file.read().strip().split('\n')

n = int(inpu.pop(0))

friendships = {}

for i in range(n):
	x = inpu[i].split()
	friendships[int(x[0])] = int(x[1])

for i in inpu[n:-1]:
	c = [int(j) for j in i.split()]
	visited = []
	pos = c[0]
	target=c[1]
	found = True
	while pos != target:
		if pos in visited:
			found = False
			break
		visited.append(pos)
		pos = friendships[pos]
	if not found:
		print("No")
	else:
		print("Yes", len(visited)-1)