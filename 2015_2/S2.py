import sys

inp = sys.stdin.read().strip().split('\n')

J = int(inp.pop(0))
A = int(inp.pop(0))

jerseys = inp[:J]

lsize = {
	'S': 1,
	'M': 2,
	'L': 3
}

numsize = [lsize[i] for i in jerseys]

total = 0
for player in inp[J+1:]:
	if lsize[player[0]] <= numsize[int(player[2:])-1]:
		numsize[int(player[2:])-1] = 0
		total += 1
print(total)