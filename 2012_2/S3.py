import sys

x = [int(i) for i in sys.stdin.read().strip().split('\n')]

x.pop(0)

frequencies = [0 for _ in range(1000)]

for i in x:
	frequencies[i-1] += 1

mfreq = max(frequencies)
tops = [f for f in range(len(frequencies)) if frequencies[f] == mfreq]

second = -1
for f in range(len(frequencies)):
	if frequencies[f] > second and frequencies[f] < mfreq:
		second = frequencies[f]
seconds = [f for f in range(len(frequencies)) if frequencies[f] == second]

if len(tops) > 1:
	print(tops[-1]-tops[0])
elif len(seconds) > 1:
	print(max(abs(tops[0]-seconds[0]), abs(seconds[-1]-tops[0])))
else:
	print(abs(tops[0]-seconds[0]))