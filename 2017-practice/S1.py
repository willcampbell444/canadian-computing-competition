import sys

nu = int(input())

count = 0
for n in range(0, 6):
	for l in range(n, 6):
		if n + l == nu:
			count += 1

print(count)