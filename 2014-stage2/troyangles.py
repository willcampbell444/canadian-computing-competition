with open("troyangles.in") as file:
	inpu = file.read().strip().split('\n')[1:]

grid = []

for i in inpu:
	grid.append([True if j == "#" else False for j in i])

# A bit too slow:

count = 0
for r in range(len(grid)):
	for c in range(len(grid[r])):
		if grid[r][c]:
			count += 1
			w = 1
			s = True
			for n in range(r+1, len(grid)):
				for nc in range(c-w, c+w+1):
					if nc < 0 or nc > len(grid)-1 or not grid[n][nc]:
						s = False
						break
				if not s:
					break
				count += 1
				w += 1


#almost works

# count = 0
# for r in reversed(range(len(grid))):
# 	for c in range(len(grid[r])):
# 		w = 0
# 		if grid[r][c]:
# 			count += 1
# 			w += 1
# 			if w > 1 and w % 2 = 1:
# 				mc = int(w/2)
# 				fail = False
# 				for rr in reversed(range(r-int(w/2), r)):
# 					for cc in range(mc-(w-(r-rr)), mc+(w-(r-rr))):
# 						if not grid[rr][cc]:
# 							fail = True
# 							break


# 		else:
# 			w = 0



print(count)