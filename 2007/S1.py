with open("S1.in") as file:
	inpu = file.read().strip().split('\n')[1:]

for i in inpu:
	p = [int(j) for j in i.split()]

	if p[0] < 1989:
		print("Yes")
	elif p[0] == 1989:
		if p[1] < 2:
			print("Yes")
		elif p[1] == 2:
			if p[2] < 28:
				print("Yes")
			else:
				print("No")
		else:
			print("No")
	else:
		print("No")