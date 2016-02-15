import sys

# with open("S1.in") as file:
# 	inpu = file.read().strip()

inpu = sys.stdin.read().strip()

target = int(inpu)

correct = []
for i in range(6):
	for j in range(6):
		if i+j == target:
			if i >= j:
				if [i, j] not in correct:
					correct.append([i, j])
			else:
				if [j, i] not in correct:
					correct.append([j, i])

print(len(correct))
