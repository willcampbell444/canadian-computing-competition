# PERFECT, ~ 10 min

with open("S1.in") as file:
	inpu = int(file.read())

count = 0

for i in range(inpu-1):
	for j in range(inpu-1):
		for k in range(inpu-1):
			if k > j and j > i:
				count += 1

print(count)