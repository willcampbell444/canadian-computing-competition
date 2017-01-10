import sys

inpu = sys.stdin.read().strip().split('\n')
sp = [int(inpu[0].split()[0]), int(inpu[0].split()[1])]
fp = [int(inpu[1].split()[0]), int(inpu[1].split()[1])]
# sp=[4, 2]
# fp=[7, 5]

poss = [sp]
v = []

moves = [
	[2, 1],
	[2, -1],
	[-2, 1],
	[-2, -1],
	[1, 2],
	[1, -2],
	[-1, 2],
	[-1, -2]
]

def add(a, b):
	return [a[0]+b[0], a[1]+b[1]]

count = 0
while True:
	newPoses = []
	if fp in poss:
		break

	for p in poss:
		for m in moves:
			q = add(p, m)
			if q not in v and q not in newPoses and q[1] > 0 and q[1] < 9 and q[0] > 0 and q[0] < 9:
				newPoses.append(add(p, m))
	v.extend(newPoses)
	poss = newPoses
	count += 1

print(count)