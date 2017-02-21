import sys

inp = sys.stdin.readlines()

inp.pop(0)

frequencies = [0 for _ in range(1000)]

for i in inp:
	frequencies[int(i)-1] += 1

highests = []
num = -1
for f in range(len(frequencies)):
	if frequencies[f] > num:
		num = frequencies[f]
		highests = [f]
	elif frequencies[f] == num:
		highests.append(f)
high = num

seconds = []
num = -1
for f in range(len(frequencies)):
	if frequencies[f] > num and frequencies[f] < high:
		num = frequencies[f]
		seconds = [f]
	elif frequencies[f] == num:
		seconds.append(f)
if len(highests) > 1:
	print(abs(highests[0]-highests[-1]))
else:
	print(max(abs(highests[0]-seconds[0]), abs(highests[0]-seconds[-1])))