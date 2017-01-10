import sys

inpu = int(sys.stdin.read().strip())

# inpu = 4

suc = []
count = 0
for i in range(6):
	for j in range(6):
		if i not in suc and j not in suc:
			if i+j == inpu:
				count += 1
	suc.append(i)

print(count)