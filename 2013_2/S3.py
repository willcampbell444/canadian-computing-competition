import sys

inp = sys.stdin.read().strip().split('\n')
T = int(inp.pop(0))
inp.pop(0)
games = [[int(j) for j in i.split()] for i in inp]
games_remaining = [(x, y) for x in range(1, 5) for y in range(x+1, 5)]

def perm(x, l):
	if l == 1:
		return [[i] for i in x]
	z = []
	for n in range(len(x)):
		z.extend([x[n]] + i for i in perm(x, l-1))
	return z

scores = [0, 0, 0, 0]

for x in games:
	games_remaining.remove((x[0], x[1]))
	if x[2] == x[3]:
		scores[x[0]-1] += 1
		scores[x[1]-1] += 1
	elif x[2] > x[3]:
		scores[x[0]-1] += 3
	elif x[2] < x[3]:
		scores[x[1]-1] += 3

wins = 0
for g in perm([1, 2, 3], len(games_remaining)):
	s = scores[:]
	for i in range(len(games_remaining)):
		if g[i] == 1:
			s[games_remaining[i][0]-1] += 3
		elif g[i] == 2:
			s[games_remaining[i][1]-1] += 3
		elif g[i] == 3:
			s[games_remaining[i][0]-1] += 1
			s[games_remaining[i][1]-1] += 1
	win = True
	for i in range(4):
		if i != T-1 and s[T-1] < s[i]:
			win = False
			break
	wins += win

print(wins)