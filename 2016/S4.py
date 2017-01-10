import sys

# brute force BFS

# with open("S4.in") as file:
inpu = sys.stdin.read().strip().split('\n')

balls = [int(i) for i in inpu[1].split()]
l = len(balls)

poss = [balls]
done = []

top = 0

while len(poss) > 0:
	done.extend(balls)
	np = []
	for p in poss:
		if max(p) > top:
			top = max(p)
		l = len(p)
		for i in range(l-1):
			if i == l-3 and p[i] == p[i+2] and p[:i]+[p[i]+p[i+1]+p[i+2]] not in done:
				np.append(p[:i]+[p[i]+p[i+1]+p[i+2]])
			elif i < l-3 and p[i] == p[i+2] and p[:i]+[p[i]+p[i+1]+p[i+2]]+p[i+3:] not in done:
				np.append(p[:i]+[p[i]+p[i+1]+p[i+2]]+p[i+3:])
			elif p[i] == p[i+1] and p[:i]+[p[i]+p[i+1]]+p[i+2:] not in done:
				np.append(p[:i]+[p[i]+p[i+1]]+p[i+2:])
	poss = np

print(top)