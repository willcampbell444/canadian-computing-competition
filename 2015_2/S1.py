import sys

inp = [int(i) for i in sys.stdin.read().strip().split('\n')[1:]]

stack = []

for x in inp:
	if x == 0:
		stack.pop()
	else:
		stack.append(x)

print(sum(stack))