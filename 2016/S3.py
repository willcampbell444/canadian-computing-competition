import sys

# start at a pho restauraunt, get rid of all the pointless parts

# with open("S3.in") as file:
# 	inpu = file.read().strip().split('\n')

inpu = sys.stdin.read().strip().split('\n')

nr = int(inpu[0].split()[0])
m = [int(i) for i in inpu[1].split()]

tree = {i:[] for i in range(nr)}

for i in inpu[2:]:
	i = i.split()
	tree[int(i[0])].append(int(i[1]))
	tree[int(i[1])].append(int(i[0]))

visited = []

def traverse(pos):
	success = False

	visited.append(pos)
	for i in tree[pos]:
		if i not in visited:
			if not traverse(i):
				tree.pop(i)
			else:
				success = True

	if pos in m:
		return True
	else:
		return success

traverse(m[0])

k = tree.keys()
for i in k:
	for j in tree[i]:
		if j not in k:
			tree[i].remove(j)

# # def go(pos):
# # 	# print(pos)
# # 	visited.append(pos)
# # 	s = 0
# # 	stuck = True
# # 	for i in tree[pos]:
# # 		if i not in visited:
# # 			stuck = False
# # 			return 1+go(i)
# # 	if stuck:
# # 		return s+1
# # 	return s

# def trip(pos):
# 	visited.append(pos)
# 	s = 0
# 	for i in tree[pos]:
# 		if i not in visited:
# 			return 1+trip(i)
# 	return s


# score = 0
# visited = []

# # for i in m:
# # 	if i not in visited:
# # 		score = trip(i)
# # 		print(i, visited, score)
# print(trip(m[0]))

shortest = 101010101001

count = 0
positions = [min(m)]
while max(m) not in positions:
	count += 1
	np = []
	for i in positions:
		for j in tree[i]:
			if j not in positions and j not in np:
				np.append(j)
	positions = np

print(count)
