# PERFECT, ~15 min

with open('S2.in') as file:
	inpu = file.read().strip()

numerals = {
	'I': 1,
	'V': 5,
	'X': 10,
	'L': 50,
	'C': 100,
	'D': 500,
	'M': 1000
}

numbers = []

count = 0
while count < len(inpu):
	numbers.insert(0, [int(inpu[count]), numerals[inpu[count+1]]])
	count += 2

prev = 0
total = 0

for n in numbers:
	if prev <= n[1]:
		total += n[0]*n[1]
	else:
		total -= n[0]*n[1]
	prev = n[1]

print(total)