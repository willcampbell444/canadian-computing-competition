# DOes not really work

with open("S4.in") as file:
	input = [i.split() for i in file.readlines()]

hull = input[0][0]
start = input[-1][0]
destination = input[-1][1]
routes = input[1:-1]

maxTime = -1

def move(ship):
	global maxTime
	if ship["hull"] <= 0:
		return -1
	elif ship["island"] == destination:
		if ship["time"] > maxTime:
			maxTime = ship["time"]
		return
	elif ship["time"] < maxTime:
		return
	ship["visited"].append(ship["island"])

	paths = []
	for i in routes:
		if i[0] == ship["island"]:
			if i[1] not in ship["visited"]:
				paths.append(i)
		elif i[1] == ship["island"]:
			if i[0] not in ship["visited"]:
				paths.append([i[1], i[0], i[2], i[3]])

	for i in paths:
		ship["hull"] -= int(i[3])
		ship["time"] += int(i[2])
		ship["island"] = i[1]

		move(ship)

move({
	"hull": int(hull),
	"time": 0,
	"island": start,
	"visited": []
})

print(maxTime)