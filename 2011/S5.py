# 23 - works, way too slow

with open("S5.in") as file:
	inpu = file.read().strip().split('\n')

possibleLights = [ [int(i) for i in inpu[1:]] ]
checked = []

def switch(lightb):
	consec = 0
	for n in range(len(lightb)):
		if lightb[n]:
			consec += 1
		elif consec >= 4:
			for m in range(n-consec, n):
				lightb[m] = 0
			consec = 0
		else:
			consec = 0
	if consec >= 4:
		for m in range(n-consec, len(light)):
			lightb[m] = 0

done = False
count = -1
while not done:
	newLights = []
	count += 1

	checked.extend(possibleLights)

	for light in possibleLights:
		for n in range(len(light)):
			if not light[n]:
				temp = light[:]
				temp[n] = 1
				switch(temp)
				if temp not in checked:
					newLights.append(temp)

	for light in possibleLights:
		if sum(light) == 0:
			done = True
			break

	possibleLights = newLights

print(count)