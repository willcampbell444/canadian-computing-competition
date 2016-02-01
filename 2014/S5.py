with open("S5.in") as file:
	inpu = file.read().split("\n")

locations = [[int(j) for j in i.split()] for i in inpu[1:]]

def distanceBetween(a, b):
	return (a[0]-b[0])**2 + (a[1]-b[1])**2

paths = [[distanceBetween(location, l) for l in locations] for location in [[0, 0]]+locations]

# Bad solution, does not really work

# def goToFarthest(point, maximum=False):
# 	target = []
# 	distanceToTarget = 0

# 	for location in locations:
# 		distance = distanceBetween(point, location)
# 		if (maximum and distance < maximum and distance > distanceToTarget) or (not maximum and distance > distanceToTarget):
# 			target = location
# 			distanceToTarget = distance

# 	if target != []:
# 		print(target, distanceToTarget)
# 		return goToFarthest(target, distanceToTarget) + 1
# 	else:
# 		print(target)
# 		return 0

# print(goToFarthest([0, 0]))



# Brute force recursion failed

# def checkAll(point, maximum=False):
# 	possiblePaths = paths[point+1]

# 	if maximum and min(possiblePaths) > maximum:
# 		return 0

# 	# print([[i, possiblePaths[i]] for i in range(len(possiblePaths)) if (maximum and possiblePaths[i] < maximum) or not maximum])
# 	return max([checkAll(i, possiblePaths[i]) for i in range(len(possiblePaths)) if (maximum and possiblePaths[i] < maximum) or not maximum])+1



# Will work sometimes

def goToBest(point, maximum=False):
	possiblePaths = paths[point+1]

	rating = []
	for i in range(len(possiblePaths)):
		if maximum and possiblePaths[i] >= maximum or point == i:
			rating.append(-1)
		else:
			rating.append(sum((j for j in paths[i+1] if j < possiblePaths[i])))

	if sum(rating) == -len(possiblePaths):
		return 0

	target = rating.index(max(rating))
	distanceToTarget = possiblePaths[target]

	return goToBest(target, distanceToTarget) + 1

print(goToBest(-1))