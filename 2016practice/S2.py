import sys

# with open("S2.in") as file:
# 	inpu = file.read().strip().split('\n')

inpu = sys.stdin.read().strip().split('\n')

h = int(inpu[0])
m = int(inpu[1])

altitude = 1
count = 0

while altitude > 0 and count < m:
	count += 1

	altitude = -6*count**4 + h*count**3 + 2*count**2 + count


if count == m:
	print("The balloon does not touch ground in the given time.")
else:
	print("The balloon first touches ground at hour:\n"+str(count))