# PERFECT, 45min

with open("S4.in") as file:
	inpu = file.read().strip().split('\n')

avalable = [int(i) for i in inpu[0].split()]
requested = [int(i) for i in inpu[1].split()]

satisfied = 0

# O- blood
if avalable[0] >= requested[0]:
	satisfied += requested[0]
	avalable[0] -= requested[0]
	requested[0] = 0
else:
	satisfied += avalable[0]
	requested[0] -= avalable[0]
	avalable[0] = 0

# O+ blood
if avalable[1] >= requested[1]:
	satisfied += requested[1]
	avalable[1] -= requested[1]
	requested[1] = 0
else:
	satisfied += avalable[1]
	requested[1] -= avalable[1]
	avalable[1] = 0
	if avalable[0] >= requested[1]:
		satisfied += requested[1]
		avalable[0] -= requested[1]
		requested[1] = 0
	else:
		satisfied += avalable[0]
		requested[1] -= avalable[0]
		avalable[0] = 0

# A- blood
if avalable[2] >= requested[2]:
	satisfied += requested[2]
	avalable[2] -= requested[2]
	requested[2] = 0
else:
	satisfied += avalable[2]
	requested[2] -= avalable[2]
	avalable[2] = 0
	if avalable[0] >= requested[2]:
		satisfied += requested[2]
		avalable[0] -= requested[2]
		requested[2] = 0
	else:
		satisfied += avalable[0]
		requested[2] -= avalable[0]
		avalable[0] = 0

# A+ blood
if avalable[3] >= requested[3]:
	satisfied += requested[3]
	avalable[3] -= requested[3]
	requested[3] = 0
else:
	satisfied += avalable[3]
	requested[3] -= avalable[3]
	avalable[3] = 0
	if avalable[2] >= requested[3]:
		satisfied += requested[3]
		avalable[2] -= requested[3]
		requested[3] = 0
	else:
		satisfied += avalable[2]
		requested[3] -= avalable[2]
		avalable[2] = 0
		if avalable[1] >= requested[3]:
			satisfied += requested[3]
			avalable[1] -= requested[3]
			requested[3] = 0
		else:
			satisfied += avalable[1]
			requested[3] -= avalable[1]
			avalable[1] = 0
			if avalable[0] >= requested[3]:
				satisfied += requested[3]
				avalable[0] -= requested[3]
				requested[3] = 0
			else:
				satisfied += avalable[0]
				requested[3] -= avalable[0]
				avalable[0] = 0

# B- blood
if avalable[4] >= requested[4]:
	satisfied += requested[4]
	avalable[4] -= requested[4]
	requested[4] = 0
else:
	satisfied += avalable[4]
	requested[4] -= avalable[4]
	avalable[4] = 0
	if avalable[0] >= requested[4]:
		satisfied += requested[4]
		avalable[0] -= requested[4]
		requested[4] = 0
	else:
		satisfied += avalable[0]
		requested[4] -= avalable[0]
		avalable[0] = 0

# B+ blood
if avalable[5] >= requested[5]:
	satisfied += requested[5]
	avalable[5] -= requested[5]
	requested[5] = 0
else:
	satisfied += avalable[5]
	requested[5] -= avalable[5]
	avalable[5] = 0
	if avalable[4] >= requested[5]:
		satisfied += requested[5]
		avalable[4] -= requested[5]
		requested[5] = 0
	else:
		satisfied += avalable[4]
		requested[5] -= avalable[4]
		avalable[4] = 0
		if avalable[1] >= requested[5]:
			satisfied += requested[5]
			avalable[1] -= requested[5]
			requested[5] = 0
		else:
			satisfied += avalable[1]
			requested[5] -= avalable[1]
			avalable[1] = 0
			if avalable[0] >= requested[5]:
				satisfied += requested[5]
				avalable[0] -= requested[5]
				requested[5] = 0
			else:
				satisfied += avalable[0]
				requested[5] -= avalable[0]
				avalable[0] = 0

# AB-
if avalable[0] >= requested[6]:
	satisfied += requested[6]
	avalable[0] -= requested[6]
	requested[6] = 0
else:
	satisfied += avalable[0]
	requested[6] -= avalable[0]
	avalable[0] = 0
	if avalable[2] >= requested[6]:
		satisfied += requested[6]
		avalable[2] -= requested[6]
		requested[6] = 0
	else:
		satisfied += avalable[2]
		requested[6] -= avalable[2]
		avalable[2] = 0
		if avalable[4] >= requested[6]:
			satisfied += requested[6]
			avalable[4] -= requested[6]
			requested[6] = 0
		else:
			satisfied += avalable[4]
			requested[6] -= avalable[4]
			avalable[4] = 0
			if avalable[6] >= requested[6]:
				satisfied += requested[6]
				avalable[6] -= requested[6]
				requested[6] = 0
			else:
				satisfied += avalable[6]
				requested[6] -= avalable[6]
				avalable[6] = 0

# AB+
for i in range(len(avalable)):
	if avalable[i] >= requested[7]:
		satisfied += requested[7]
		avalable[i] -= requested[7]
		requested[7] = 0
	else:
		satisfied += avalable[i]
		requested[7] -= avalable[i]
		avalable[i] = 0

print(satisfied)