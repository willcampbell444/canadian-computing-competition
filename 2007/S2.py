with open("S2.in") as file:
	inpu = file.read().strip().split('\n')

n = int(inpu[0])

bigs = [ sorted([int(j) for j in i.split()]) for i in inpu[1:n+1]]
smalls = [ sorted([int(j) for j in i.split()]) for i in inpu[n+2:]]

bigs.sort(key=lambda x: x[0]*x[1]*x[2])


for s in smalls:
	fit = False
	for b in bigs:
		if s[0] <= b[0] and s[1] <= b[1] and s[2] <= b[2]:
			fit = True
			print(b[0]*b[1]*b[2])
			break
	if not fit:
		print("Item does not fit.")