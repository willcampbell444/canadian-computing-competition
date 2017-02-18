import sys

inp = sys.stdin.readlines()

numbox = int(inp.pop(0))

boxes = [sorted([int(j) for j in i.split()]) for i in inp[:numbox]]
items = [sorted([int(j) for j in i.split()]) for i in inp[numbox+1:]]

boxes.sort(key = lambda x: x[0]*x[1]*x[2])

for item in items:
	printed = False
	for box in boxes:
		if item[0] <= box[0] and item[1] <= box[1] and item[2] <= box[2]:
			print(box[0]*box[1]*box[2])
			printed = True
			break
	if not printed:
		print("Item does not fit.")