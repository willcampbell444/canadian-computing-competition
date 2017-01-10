import sys

# with open("S5.in") as file:
	# inpu = file.read().strip().split('\n')
inpu = sys.stdin.read().strip().split('\n')

t = int(inpu[0].split()[1])
board = []
for i in inpu[1]:
	if i == "1":
		board.append(True)
	else:
		board.append(False)

l = len(board)

pattern = []

count = 0
while count < t:
	pattern.append(board)
	count += 1
	nb = board[:]

	for i in range(l):
		if i == l-1:
			if board[i-1] != board[0]:
				nb[i] = True
			else:
				nb[i] = False
		else:
			if board[i-1] != board[i+1]:
				nb[i] = True
			else:
				nb[i] = False
	board = nb
	if board in pattern:
		ppp = pattern.index(board)
		pattern = pattern[ppp:]
		board = pattern[(t-ppp)%len(pattern)]
		break

# for j in pattern:
# 	str = ""
# 	for i in j:
# 		if i:
# 			str += "1"
# 		else:
# 			str += "0"
# 	print(str)

str = ""
for i in board:
	if i:
		str += "1"
	else:
		str += "0"

print(str)