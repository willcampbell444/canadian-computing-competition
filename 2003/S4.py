import sys

inp = sys.stdin.read().split('\n')

inp.pop(0)

for s in inp:
	total = 1
	for substr_len in range(1, len(s)+1):
		substrs = set()
		for i in range(0, len(s)+1-substr_len):
			substrs.add(s[i:i+substr_len])
		total += len(substrs)
	print(total)