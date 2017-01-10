with open("S5.in") as file:
	target = int(file.read())

num = 1
points = 0
while num < target:
	num += num
	points += 1

print(num, points)