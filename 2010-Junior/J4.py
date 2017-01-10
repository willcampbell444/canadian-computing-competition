import sys

inpu = sys.stdin.read().strip().split('\n')
# with open("S4.in") as file:
	# inpu = file.read().strip().split('\n')
# inpu = """7 3 4 6 4 5 7 5
# 3 1 3 5
# 3 1 4 5
# 4 3 4 6 7
# 0""".strip().split('\n')

def start(a, b):
	win = True
	for i in range(len(b)):
		if a[i] != b[i]:
			return False
	return True

for i in inpu[:-1]:
	dif = []
	ne = [int(j) for j in i.split()[1:]]

	for n in range(1, len(ne)):
		dif.append(ne[n]-ne[n-1])
	win = False
	# for n in range(int(len(dif)/2)+1):
	# 	print(dif, dif[:n+1], dif[n+1:n+n+2])
	# 	if dif[:n+1] == dif[n+1:n+n+2]:
	# 		print(n+1)
	# 		win = True
	# 		break
	# if not win:
	# 	print(len(dif), "HHOH")
	for n in range(1, len(dif)):
		if dif[n] == dif[0]:
			if start(dif[:n], (dif[n:n+n])) and start(dif[:n], dif[n+n:n+n+n]):
				print(n)
				win = True
				break
	if not win:
		print(len(dif))

	# print(len(dif))