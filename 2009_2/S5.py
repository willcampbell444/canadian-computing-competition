import sys, math

inp = sys.stdin.readlines()

cityWidth = int(inp.pop(0))
cityHeight = int(inp.pop(0))
inp.pop(0)

shops = [[0 for _ in range(cityWidth)] for _ in range(cityHeight)]
total = 0
for signal in inp:
	s = signal.split()
	print(s)
	x = int(s[0])-1
	y = int(s[1])-1
	radius = int(s[2])
	rsq = radius * radius
	strength = int(s[3])
	if y-radius < -20 and y+radius > cityWidth+20:
		total += strength
	else:
		for height in range(max(x-radius, 0), min(x+radius+1, cityHeight)):
			width = int(math.sqrt(rsq - (height-x)*(height-x)))
			for w in range(max(y-width, 0), min(y+width+1, cityWidth)):
				shops[height][w] += strength

maxStrength = -1
count = 0
for row in shops:
	for strength in row:
		if strength > maxStrength:
			maxStrength = strength
			count = 1
		elif strength == maxStrength:
			count += 1

print(maxStrength+total)
print(count)