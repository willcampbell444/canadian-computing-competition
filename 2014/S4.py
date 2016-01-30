with open("S4.in") as file:
	inpu = file.read().split('\n')

threshold = int(inpu[1])
peices = [[int(j) for j in i.split()] for i in inpu[2:]]


windowWidth = 0
windowHeight = 0

for i in peices:
	if i[2] > windowWidth:
		windowWidth = i[2]
	if i[3] > windowHeight:
		windowHeight = i[3]

array = [[0 for j in range(windowHeight)] for i in range(windowWidth)]

for i in peices:
	for x in range(i[0], i[2]):
		for y in range(i[1], i[3]):
			array[x][y] += i[4]

total = 0

for column in array:
	for node in column:
		if node >= threshold:
			total += 1

print(total)