# PERFECT WOHOHOH

import math

with open("S2.in") as file:
	inpu = file.read().strip().split('\n')

for c in inpu[:-1]:
	radius = int(c)
	radiusSq = radius*radius

	# count = 0
	# for i in range(1, radius+1):
	# 	for j in range(1, radius+1):
	# 		if i*i + j*j <= radiusSq:
	# 			count += 1

	count = 0
	for i in range(1, radius+1):
		w = int(math.sqrt((radius*radius)-i*i))

		count += w

	print((count*4)+(radius*4)+1)