import sys

inp = sys.stdin.readlines()

h = int(inp[0])
m = int(inp[1])

hour = 1
won = False

while hour <= m:
	alt = -6*hour**4 + h*hour**3 + 2*hour**2 + hour

	if alt <= 0:
		won = True
		break

	hour += 1

if won:
	print("The balloon first touches ground at hour:")
	print(hour)
else:
	print("The balloon does not touch ground in the given time.")