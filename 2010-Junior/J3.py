import sys

inpu = sys.stdin.read().strip().split('\n')

dd = {"A": 0, "B": 0}

for i in inpu:
	i = i.split()

	if i[0] == "1":
		dd[i[1]] = int(i[2])
	elif i[0] == "2":
		print(dd[i[1]])
	elif i[0] == "3":
		dd[i[1]] = dd[i[1]] + dd[i[2]]
	elif i[0] == "4":
		dd[i[1]] = dd[i[1]] * dd[i[2]]
	elif i[0] == "5":
		dd[i[1]] = dd[i[1]] - dd[i[2]]
	elif i[0] == "6":
		dd[i[1]] = int(dd[i[1]]/dd[i[2]])
	elif i[0] == "7":
		break