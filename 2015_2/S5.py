# a b

# max = max(a.left, b.all | a.all, b.right)

import sys

def maxi(stuff, pos=0):
	if len(stuff)-pos == 1:
		return stuff[pos]
	elif len(stuff)-pos == 2:
		return max(stuff[pos], stuff[pos+1])
	return max(stuff[pos]+maxi(stuff, pos+2), maxi(stuff, pos+1))

inp = sys.stdin.read().strip().split('\n')
x = [int(i) for i in inp[1:-1]]
print(maxi(x))