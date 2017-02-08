import sys

inp = sys.stdin.read().strip().split('\n')
vowels = "aeiouy "
def lastSyl(x):
	p = len(x)-1
	while x[p] not in vowels:
		p -= 1
	p += 1
	return x[p:]

inp.pop(0)

for x in range(0, len(inp), 4):
	n1 = lastSyl(inp[x])
	n2 = lastSyl(inp[x+1])
	n3 = lastSyl(inp[x+2])
	n4 = lastSyl(inp[x+3])

	if n1 == n2 == n3 == n4:
		print("perfect")
	elif n1 == n2 and n3 == n4:
		print("even")
	elif n1 == n3 and n2 == n4:
		print("cross")
	elif n1 == n4 and n2 == n3:
		print("shell")
	else:
		print("free")

