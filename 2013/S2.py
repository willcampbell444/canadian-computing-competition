# ALMOST PERFECT, 2.6.in was wrong

with open("S2.in") as file:
	inpu = [int(i) for i in file.readlines()]

maxWeight = inpu[0]
cars = inpu[2:]

bridge = []
count = -1

def next():
	if len(bridge) == 4:
		bridge.pop()
	bridge.insert(0, cars.pop(0))

while len(cars) > 0 and sum(bridge) <= maxWeight:
	count += 1
	next()

print(count)