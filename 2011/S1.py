# PERFECT, 3 min

with open("S1.in") as file:
	text = file.read()

t = 0
s = 0

for char in text.lower():
	if char == 't':
		t += 1
	elif char == 's':
		s += 1

if t > s:
	print("English")
else:
	print("French")