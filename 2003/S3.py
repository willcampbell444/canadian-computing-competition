import sys

inp = sys.stdin.read().strip().split('\n')

tiles = int(inp.pop(0))
inp.pop(0)
inp.pop(0)

marked = [[False for _ in i] for i in inp]
roomSizes = []

def size(r, c):
	global inp, marked
	marked[r][c] = True
	total = 1
	for rr, cc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
		if rr >= 0 and rr < len(inp):
			if cc >= 0 and cc < len(inp[0]):
				if not marked[rr][cc] and inp[rr][cc] == ".":
					total += size(rr, cc)
	return total

for row in range(len(inp)):
	for column in range(len(inp[row])):
		if not marked[row][column] and inp[row][column] == ".":
			roomSizes.append(size(row, column))

roomSizes.sort()

filled = 0
while roomSizes:
	x = roomSizes.pop()
	if tiles-x < 0:
		break
	else:
		tiles = tiles-x
		filled += 1

print(filled, tiles)