with open("S4.in") as file:
	inpu = file.read()

def perm(stuff):
	if len(stuff) == 1:
		return [[stuff[0]]]
	perms = []
	for n in range(len(stuff)):
		perms.extend([stuff[n]]+x for x in perm(stuff[:n]+stuff[n+1:]))
	return perms

def perm2(stuff, length):
	if len(stuff) == 1:
		return [[stuff[0]]]
	if length == 1:
		return [[i] for i in stuff]
	perms = []
	for n in range(len(stuff)):
		perms.extend([stuff[n]]+x for x in perm2(stuff, length-1))
	return perms

def add(a, b):
	return a+b

def subtract(a, b):
	return a-b

def mult(a, b):
	return a*b

def div(a, b):
	if a % b != 0:
		raise ZeroDivisionError("bad")

	return a/b

operators = [add, subtract, mult, div]

inpu = inpu.split('\n')
num_hands = int(inpu.pop(0))

for case in range(num_hands):
	hand = [int(inpu.pop(0)) for i in range(4)]

	maxVal = -420
	stuff = []
	for possible_hand in perm(hand):
		for operatorz in perm2(operators, 3):
			try:
				value1 = operatorz[2](operatorz[1](operatorz[0](possible_hand[0], possible_hand[1]), possible_hand[2]), possible_hand[3])
			except:
				value1 = -1

			try:
				value2 = operatorz[0](operatorz[1](possible_hand[0], possible_hand[1]), operatorz[2](possible_hand[2], possible_hand[3]))
			except:
				value2 = -1

			value = max(value1, value2)
			
			if value > maxVal and value < 25:
				maxVal = value
				stuff = (possible_hand, operatorz)

	print(maxVal)