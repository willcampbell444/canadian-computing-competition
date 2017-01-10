import sys

with open("S1.in") as file:
	inpu = file.read().strip().split('\n')[1:]

# inpu = sys.stdin.read().strip().split('\n')[1:]

heights = {}
widths = {}

for i in inpu:
	x = i.split()
	if int(x[1]) in heights.keys():
		heights[int(x[1])].append(int(x[0]))
	else:
		heights[int(x[1])] = [int(x[0])]

	if int(x[0]) in widths.keys():
		widths[int(x[0])].append(int(x[1]))
	else:
		widths[int(x[0])] = [int(x[1])]


count = 0
for h in heights.keys():
	if len(heights[h]) > 2:
		for w in heights[h][1:-1]:
			if len(widths[w]) > 2:
				print(w, h)
				a = 0
				b = 0
				c = 0
				d = 0
				for y in widths[w]:
					if y > h:
						a += 1
					elif y < h:
						b += 1
				for y in heights[h]:
					if y > w:
						c += 1
					elif y < w:
						d += 1
				print("AA", a*b*c*d*2, a, b, c, d)
				count += a*b*c*d*2

print(count)