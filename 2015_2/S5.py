# a b

# max = max(a.left, b.all | a.all, b.right)

import sys
from collections import deque

inp = sys.stdin.read().strip().split('\n')

N = int(inp.pop(0))
n = [int(i) for i in inp[:N]]
m = [int(i) for i in inp[N+1:]]

left_firsts = [0]
first = 0
second = 0
for s in n:
	tmp = first
	first = max(first, second + s)
	second = tmp
	left_firsts.append(first)

right_firsts = [0]
first = 0
second = 0
for s in reversed(n):
	tmp = first
	first = max(first, second + s)
	second = tmp
	right_firsts.append(first)
right_firsts.reverse()

m.sort()
to_insert = deque(m)

inMax = True
while to_insert:
	maxmax = -1
	maxmin = -1
	maxminpos = -1
	maxmaxpos = -1
	for i in range(len(left_firsts)):
		xmin = left_firsts[i]+right_firsts[i]
		if xmin > maxmin:
			maxmin = xmin
			maxminpos = i
	xmax = to_insert[-1]+right_firsts[1]
	if xmax > maxmax:
		maxmax = xmax
		maxmaxpos = 0
	xmax = to_insert[-1]+left_firsts[-2]
	if xmax > maxmax:
		maxmax = xmax
		maxmaxpos = len(left_firsts)-1
	for i in range(1, len(left_firsts)-1):
		xmax = left_firsts[i-1]+to_insert[-1]+right_firsts[i+1]
		if xmax > maxmax:
			maxmax = xmax
			maxmaxpos = i

	if maxmax >= maxmin:
		n.insert(maxmaxpos, to_insert.pop())
	else:
		n.insert(maxminpos, to_insert.popleft())

	left_firsts = [0]
	first = 0
	second = 0
	for s in n:
		tmp = first
		first = max(first, second + s)
		second = tmp
		left_firsts.append(first)

	right_firsts = [0]
	first = 0
	second = 0
	for s in reversed(n):
		tmp = first
		first = max(first, second + s)
		second = tmp
		right_firsts.append(first)
	right_firsts.reverse()

# print(n)
# print(left_firsts)
# print(right_firsts)
print(right_firsts[0])

# add_max(30)
# add_min(1)
# add_max(1)


# inMax = True
# while to_insert:
# 	if add_max(right_firsts, left_firsts)
# m = [1]
# if len(m) == 1:
# 	with_m = []
# 	for i in range(len(left_firsts)-1):
# 		with_m.append(max(left_firsts[i]+right_firsts[i], left_firsts[i-1]+m[0]+right_firsts[i+1]))
# 	print(max(with_m))
# 	print(with_m)
# else:
# 	print(right_firsts[0])