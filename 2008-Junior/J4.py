import sys

inpu = sys.stdin.read().strip().split('\n')[:-1]
# inpu = ["- - 3 + 2 1 9"]

def post(dank):
	if dank[0] in "0123456789":
		return [dank[0]]
	else:
		count = 1
		n = 0
		while n < 1:
			if str(dank[count]) in "0123456789":
				n += 1
			else:
				n -= 1
			count += 1
		return post(dank[1:count]) + post(dank[count:]) + [dank[0]]

for i in inpu:
	inf = i.split()

	out = post(inf)
	print(' '.join(out))