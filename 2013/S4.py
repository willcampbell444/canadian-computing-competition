with open("S4.in") as file:
	inpu = file.read().split('\n')

students = int(inpu[0].split()[0])
measurements = [[int(j) for j in i.split()] for i in inpu[1:-1]]
p = int(inpu[-1].split()[0])
q = int(inpu[-1].split()[1])

# Check if p is taller then q
shorter = []
taller = []
removed = True

for i in measurements:
	if i[0] == p:
		shorter.append(i[1])
		measurements.remove(i)
	elif i[1] == p:
		taller.append(i[0])
		measurements.remove(i)

while removed and q not in taller and q not in shorter:
	removed = False
	for j in measurements:
		for i in taller:
			if j[1] == i:
				taller.append(j[0])
				measurements.remove(j)
				removed = True
		for i in shorter:
			if j[0] == i:
				shorter.append(j[1])
				measurements.remove(j)
				removed = True

if q in shorter:
	print("yes")
elif q in taller:
	print("no")
else:
	print("unknown")