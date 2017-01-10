import sys

# with open("S1.in") as file:
inpu = sys.stdin.read().strip().split('\n')

str1 = [ i for i in inpu[0] ]
str2 = [ i for i in inpu[1] ]

a = True

for char in str1:
	if len(str2) == 0:
		a = False
		break
	elif char in str2:
		str2.remove(char)
	elif "*" in str2:
		str2.remove("*")

if a and len(str2) == 0:
	print("A")
else:
	print("N")