# CORRECT, BUT WAY TOO SLOW, USES TOO MUCH SPACE

with open("S4.in") as file:
	inpu = file.readlines()#.split('\n')

threshold = int(inpu[1])
peices = [[int(j) for j in i.split()] for i in inpu[2:]]


windowWidth = 0
windowHeight = 0

for i in peices:
	if i[2] > windowWidth:
		windowWidth = i[2]
	if i[3] > windowHeight:
		windowHeight = i[3]

print("Found width, height")

array = [[0 for j in range(windowHeight)] for i in range(windowWidth)]

print("Initialied array")

print("Filling array...")
for i in peices:
	if peices.index(i) % 50 == 0:
		print(" >> Peice", peices.index(i), "filled!")
	for x in range(i[0], i[2]):
		for y in range(i[1], i[3]):
			array[x][y] += i[4]

total = 0
print("Counting total")

for column in array:
	for node in column:
		if node >= threshold:
			total += 1

print(total)