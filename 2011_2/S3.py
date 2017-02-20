import sys

inp = sys.stdin.readlines()

inp.pop(0)

winners = {(1, 0), (2, 0), (3, 0), (2, 1)}
flux = {(1, 1), (2, 2), (3, 1)}

def check(level, x, y):
	global winners, flux

	if level == 1:
		return (x, y) in winners
	if (x//5**(level-1), (y//5**(level-1))) in winners:
		return True
	elif (x//5**(level-1), (y//5**(level-1))) in flux:
		return check(level - 1, x%5**(level-1), y%5**(level-1))
	return False


for line in inp:
	line = line.split()
	mlevel = int(line[0])
	x = int(line[1])
	y = int(line[2])

	if check(mlevel, x, y):
		print("crystal")
	else:
		print("empty")