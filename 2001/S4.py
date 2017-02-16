import sys

inp = sys.stdin.read().split('\n')
inp.pop(0)

m = -1
for x in inp:
	z = x.split()
	print(z)
	z = int(z[0])**2 + int(z[1])**2
	print(z)
	if z > m:
		m = z
m = m**(1/2)

print("{0:.2f}".format(m))