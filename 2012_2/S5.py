import sys

inp = sys.stdin.read().strip().split('\n')

x = inp.pop(0).split()
R = max(int(x[0]), int(x[1]))
C = min(int(x[0]), int(x[1]))

spots = [[0 for _ in range(C)] for _ in range(R)]
filled = [[False for _ in range(C)] for _ in range(R)]
spots[0][0] = 1

inp.pop(0)
for x in inp:
	x = x.split()
	filled[int(x[1])-1][int(x[0])-1] = True

for c in range(R-1, -R, -1):
	for z in range(R-c+1):
		if z < C and R-c-z < R and not filled[R-c-z][z]:
			if R-c-z-1 < R:
				spots[R-c-z][z] += spots[R-c-z-1][z]
			if z-1 > -1:
				spots[R-c-z][z] += spots[R-c-z][z-1]

print(spots[-1][-1])