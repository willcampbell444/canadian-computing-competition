# PERFECT, ~23 min

with open("S3.in") as file:
	inpu = file.read().strip().split('\n')

sensors = inpu[1:]

# frequencies = [0 for i in range(1000)]

frequencies = {}

for i in range(1000):
	frequencies[i+1] = 0

for i in sensors:
	frequencies[int(i)] += 1

first = 0
firstReadings = []
second = 0
secondReadings = []

for i in range(1000):
	if frequencies[i+1] > first:
		firstReadings = [i+1]
		first = frequencies[i+1]
	elif frequencies[i+1] == first:
		firstReadings.append(i+1)
	elif frequencies[i+1] > second:
		secondReadings = [i+1]
		second = frequencies[i+1]
	elif frequencies[i+1] == second:
		secondReadings.append(i+1)

if max(firstReadings) > max(secondReadings):
	print(max(firstReadings)-min(secondReadings))
else:
	print(max(secondReadings)-min(firstReadings))