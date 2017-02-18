import sys

inp = sys.stdin.readlines()

classSize = int(inp.pop(0))

relationships = {}
for r in inp[:classSize]:
	r = r.split()
	relationships[int(r[0])] = int(r[1])

for x in inp[classSize:-1]:
	x = x.split()
	a = int(x[0])
	b = int(x[1])
	marked = set()
	marked.add(a)
	count = -1
	while a != b and a in relationships:
		if relationships[a] not in marked:
			count += 1
			a = relationships[a]
			marked.add(a)
		else:
			print("No")
			break
	if a == b:
		print("Yes", count)