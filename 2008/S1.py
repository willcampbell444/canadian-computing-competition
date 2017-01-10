# 5:55 - perfect, 4 min

with open("S1.in") as file:
	inpu = file.read().strip().split('\n')

coldest = ""
temp = 250

for i in inpu:
	i = i.split()

	if int(i[1]) < temp:
		coldest = i[0]
		temp = int(i[1])

print(coldest)