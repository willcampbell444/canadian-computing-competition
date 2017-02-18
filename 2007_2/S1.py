import sys

inp = sys.stdin.readlines()

inp.pop(0)

electionDate = [2007, 2, 27]

for i in inp:
	i = [int(j) for j in i.split()]
	i[0] += 18
	if i[0] < electionDate[0]:
		print("Yes")
	elif i[0] == electionDate[0]:
		if i[1] < electionDate[1]:
			print("Yes")
		elif i[1] == electionDate[1]:
			if i[2] <= electionDate[2]:
				print("Yes")
			else:
				print("No")
		else:
			print("No")
	else:
		print("No")