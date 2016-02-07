# WORKS, BUT WAY TOO SLOW, ~20 min
# FIXED IT, TOKK A WHILE

with open("S5.in") as file:
	inpu = file.read().strip().split('\n')

rows = int(inpu[0].split()[0])
columns = int(inpu[0].split()[1])

cats = [ [int(j) for j in i.split()] for i in inpu[2:]]

positions = [(1, 1)]

count = 0

# while True:
# 	newPositions = []

# 	for pos in positions:
# 		if pos[0] < rows and [pos[0]+1, pos[1]] not in cats:
# 			newPositions.append((pos[0]+1, pos[1]))
# 		if pos[1] < columns and [pos[0], pos[1]+1] not in cats:
# 			newPositions.append((pos[0], pos[1]+1))

# 	if not newPositions:
# 		break

# 	positions = newPositions

# 	count += 1
# 	if count == rows+columns:
# 		break

# 	print(count)

# print(len(positions))

positions = [[0 for c in range(columns)] for r in range(rows)]
for i in cats:
	positions[i[0]-1][i[1]-1] = -1

blankMap = [m[:] for m in positions]

positions[0][0] = 1

count = 0

while True:
	newPositions = [m[:] for m in blankMap]

	for row in range(rows):
		for column in range(columns):
			if positions[row][column] > 0:
				if row != rows-1 and positions[row+1][column] != -1:
					newPositions[row+1][column] += positions[row][column]
				if column != columns-1 and positions[row][column+1] != -1:
					newPositions[row][column+1] += positions[row][column]

	positions = newPositions

	count += 1
	if positions[-1][-1] > 0 or positions == blankMap:
		break

print(positions[-1][-1])