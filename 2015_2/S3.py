import sys

inp = sys.stdin.read().strip().split('\n')

G = int(inp.pop(0))
inp.pop(0)

loaded = 0
gates = [False for i in range(G)]
for plane in inp:
	plane = int(plane)-1
	while plane > -1 and gates[plane]:
		plane -= 1
	if plane > -1:
		loaded += 1
		gates[plane] = True
	else:
		break
print(loaded)
