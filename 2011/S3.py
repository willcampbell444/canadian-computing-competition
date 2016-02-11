# ALMOST PERFECT, I THINK THE TEST INPUTS ARE WRONG, 1:05 hours

with open("S3.in") as file:
	inpu = file.read().strip().split('\n')

cases = [ [int(j) for j in i.split()] for i in inpu[1:]]
cases = [{"m": case[0], "x": case[1], "y": case[2]} for case in cases]

for case in cases:
	width = 5**case['m']
	if case['x'] < width/5 or case['x'] >= (width/5)*4:
		print("empty")
	elif case['y'] > int(width/2):
		print("empty")
	elif case['x'] < (width/5)*2:
		cell = case['x']-(width/5)
		height = (width/5)-1
		if cell < width/10:
			height += cell
		else:
			height += ((width/5)-1)-cell
		if case['y'] <= height:
			print("crystal")
		else:
			print('empty')
	elif case['x'] >= (width/5)*3:
		cell = case['x']-(width/5)*3
		height = (width/5)-1
		if cell < width/10:
			height += cell
		else:
			height += ((width/5)-1)-cell
		if case['y'] <= height:
			print("crystal")
		else:
			print('empty')
	elif case['x'] >= (width/5)*2:
		cell = case['x']-(width/5)*2
		height = ((2*width)/5)-1
		if cell < width/10:
			height += cell
		else:
			height += ((width/5)-1)-cell
		if case['y'] <= height:
			print("crystal")
		else:
			print('empty')

