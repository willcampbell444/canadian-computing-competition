# WAY TOO SLOW

with open("S1.in") as file:
	inpu = file.read().strip().split('\n')

a = int(inpu[0])
b = int(inpu[1])

squares = []

for i in range(int(b**0.5)+1):
	squares.append(i**2)

cubes = []

for i in range(int(b**(1/3))+1):
	cubes.append(i**3)


# def isCool(i):
# 	print(pow(i, 0.5)%1, pow(i, 1/3))
# 	if (i**0.5) % 1 == 0 and (i**(1/3)) % 1 == 0:
# 		return True
# 	return False
c = 0
for n in range(a, b+1):
	if n in squares and n in cubes:
		c += 1

print(c)

# 64
# 8^2
# 4^3
# 2^6


# n = x*x*x = y*y






