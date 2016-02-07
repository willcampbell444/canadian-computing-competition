# WORKS FOR INPUTS UNDER 6, ~1.5 hours

with open("S4.in") as file:
	inpu = file.read().strip().split('\n')

tests = []

count = 0
while inpu[count] != '0':
	tests.append([[int(i)] for i in inpu[count+1].split()])
	count += 2

# def solve(board):
# 	if test != sorted(test):
# 		return 0

# 	possibleMoves = []
# 	for i in test:
# 		if i != []:
# 			for j in test:
# 				if j == [] or i[-1] < j[-1]:
# 					possibleMoves.append([test.index(i), test.index(j)])

# 	newBoards = []
# 	for i in possibleMoves:




for test in tests:
	possibleBoards = [test]
	oldBoards = [test]
	target = [[i+1] for i in range(len(test))]
	count = 0
	while True:
		newPossibleBoards = []

		solved = False
		for x in possibleBoards:
			if x == target:
				print(count)
				solved = True
				break
		if solved:
			break

		frozen = True
		for x in possibleBoards:
			temp = []
			for i in range(len(x)):
				if len(x[i]) > 0:
					if i == 0:
						j = i+1
						if not x[j] or x[i][-1] < x[j][-1]:
							frozen = False
							newBoard = [m[:] for m in x]
							newBoard[j].append(newBoard[i].pop())
							if newBoard not in oldBoards:
								temp.append(newBoard)
								oldBoards.append(newBoard)
					elif i == len(x)-1:
						j = i-1
						if not x[j] or x[i][-1] < x[j][-1]:
							frozen = False
							newBoard = [m[:] for m in x]
							newBoard[j].append(newBoard[i].pop())
							if newBoard not in oldBoards:
								temp.append(newBoard)
								oldBoards.append(newBoard)
					else:
						for j in [i-1, i+1]:
							if not x[j] or x[i][-1] < x[j][-1]:
								frozen = False
								newBoard = [m[:] for m in x]
								newBoard[j].append(newBoard[i].pop())
								if newBoard not in oldBoards:
									temp.append(newBoard)
									oldBoards.append(newBoard)
			newPossibleBoards.extend(temp)

		if frozen or count > 100000 or len(possibleBoards) > 50000:
			print("IMPOSSIBLE")
			break

		possibleBoards = newPossibleBoards
		count += 1