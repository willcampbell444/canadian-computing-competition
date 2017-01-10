import sys

with open("S3.in") as file:
	inpu = file.read().strip().split('\n')

# inpu = sys.stdin.read().strip().split('\n')

height = int(inpu[0].split()[0])
blocks = [[int(j) for j in i.split()] for i in inpu[1:]]

blocks.sort(key=lambda x: x[0])

for b in blocks:
	for c in blocks:
		if c 