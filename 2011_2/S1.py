import sys

inp = sys.stdin.readlines()

inp.pop(0)

tcount = 0
scount = 0

for line in inp:
	line = line.lower()
	for char in line:
		if char == "t" or char == "T":
			tcount += 1
		elif char == "s" or char == "S":
			scount += 1

if tcount > scount:
	print("English")
else:
	print("French")