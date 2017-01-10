import sys

# with open("S3.in") as file:
# 	inpu = file.read().strip().split('\n')


inpu = sys.stdin.read().strip().split('\n')

readings = [int(i) for i in inpu[1:]]
frequencies = [0 for i in range(1000)]

for i in readings:
	frequencies[i-1] += 1

top = []
second = []
topN = -1
secondN = -1

for f in range(len(frequencies)):
	if frequencies[f] > topN:
		second = top
		secondN = topN
		top = [f+1]
		topN = frequencies[f]
	elif frequencies[f] == topN:
		top.append(f+1)
	elif frequencies[f] > secondN:
		second = [f+1]
		secondN = frequencies[f]
	elif frequencies[f] == secondN:
		second.append(f+1)

if len(top) > 1:
	print(max(top)-min(top))
elif top[0]-min(second) >= max(second)-top[0]:
	print(top[0]-min(second))
else:
	print(max(second)-top[0])