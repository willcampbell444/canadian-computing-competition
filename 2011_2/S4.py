import sys

inp = sys.stdin.readlines()

avalible = [int(i) for i in inp[0].split()]
required = [int(i) for i in inp[1].split()]

canUse = [
	[0],
	[1, 0],
	[2, 0],
	[3, 2, 1, 0], #x
	[4, 0],
	[5, 4, 1, 0], #y
	[0, 2, 4, 6],
	[1, 3, 5, 7, 0, 2, 4, 6]
]

satisfied = 0
for i in range(8):
	for j in canUse[i]:
		if avalible[j] >= required[i]:
			satisfied += required[i]
			avalible[j] -= required[i]
			required[i] = 0
		else:
			satisfied += avalible[j]
			required[i] -= avalible[j]
			avalible[j] = 0

print(satisfied)
