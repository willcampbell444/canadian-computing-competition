import sys


inpu = [int(i) for i in sys.stdin.read().strip().split('\n')]
# inpu = [4, 2, 5, 3, 12]


a = 0
aa = False
b = 0
bb = False
ac = 0
bc = 0
# a = int(inpu[4]/(inpu[0]+inpu[1]))*(inpu[0]-inpu[1]) + inpu[4]%(inpu[0]-inpu[1])
# b = int(inpu[4]/(inpu[2]+inpu[3]))*(inpu[2]-inpu[3]) + inpu[4]%(inpu[2]-inpu[3])
for i in range(1, 1+int(inpu[-1])):
	if (aa and ac % inpu[0] == 0) or (not aa and ac % inpu[1] == 0):
		ac = 0
		aa = not aa
	if (bb and bc % inpu[2] == 0) or (not bb and bc % inpu[3] == 0):
		bc = 0
		bb = not bb
	if aa:
		a += 1
	else:
		a -= 1
	if bb:
		b += 1
	else:
		b -= 1
	ac += 1
	bc += 1

if abs(a) > abs(b):
	print("Nikky")
elif abs(a) < abs(b):
	print("Byron")
else:
	print("Tied")