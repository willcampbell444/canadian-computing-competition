import sys

total = 0

n = int(sys.stdin.read())

for i in range(1, n):
	for j in range(1, i):
		total += j-1

print(total)