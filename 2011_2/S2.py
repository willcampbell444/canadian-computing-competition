import sys

inp = sys.stdin.readlines()

n = int(inp.pop(0))

score = 0
for i in range(n):
	if inp[i] == inp[n+i]:
		score += 1
print(score)