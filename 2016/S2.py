import sys


# question 1: min speed
# question 2: max speed

# Q1: sort both lists, match 0 with 0, 1 with 1, etc
# Q2: reverse list 2

# with open("S2.in") as file:
inpu = sys.stdin.read().strip().split('\n')

c1 = [int(i) for i in inpu[2].split()]
c2 = [int(i) for i in inpu[3].split()]

c1.sort()
c2.sort()

if inpu[0] == "2":
	c1.reverse()

summ = 0

for i in range(len(c1)):
	summ += max(c1[i], c2[i])

print(summ)