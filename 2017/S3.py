import sys, math

inp = sys.stdin.readlines()

heights = [0 for i in range(2000)]

for i in inp[1].split():
	i = int(i)
	heights[i-1] += 1

maxlen = -1
num_occurrances = 0
for total_height in range(2, 4001): #4001
	length = 0
	for heightOne in range(max(1, i-2000), i//2+1):
		(heightOne), (total_height - heightOne)
		if heightOne == i-h:
			length += heights[heightOne-1]//2
		else:
			length += min(heights[heightOne-1], heights[total_height-heightOne-1])

	if length > maxlen:
		maxlen = length
		num_occurrances = 1
	elif length == maxlen:
		num_occurrances += 1
print(maxlen, num_occurrances)