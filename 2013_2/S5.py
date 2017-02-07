import sys

N = int(sys.stdin.read())

cost = 0
while N > 1:
	if N % 2 == 0:
		N = N // 2
		cost += 1
	else:
		x = N//2
		while (N-x) % x != 0:
			x -= 1
		cost += (N-x) // x
		N = N-x

print(cost)