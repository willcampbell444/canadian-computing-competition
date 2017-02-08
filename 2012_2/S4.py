import sys
from collections import deque

inp = sys.stdin.read().strip().split('\n')

class moveList(list):
	def __hash__(self):
		h = 1
		for x in range(0, len(self), 2):
			if self[x]:
				h += h*self[x][-1] + self[x][-1]
			else:
				h -= x*231
		return h

while inp[0] != "0":
	pieces = [[int(i)] for i in inp[1].split()]

	queue = deque()
	queue.append((moveList(pieces), 0))

	goal = sorted(pieces)

	seen = set()
	seen.add(moveList(pieces))

	win = False

	maxx = len(pieces)

	count = 0
	while queue:
		board, moves = queue.popleft()

		if moves == count:
			count += 1
			print(count, len(seen))

		if board[-1] and board[-1][0] == maxx:
			board[-1].pop(0)
			maxx -= 1

		ml = False
		for i in range(len(board)-1):
			if board[i] and board[i][-1] == maxx and not board[i+1]:
				b = moveList([z[:] for z in board])
				b[i+1].append(b[i].pop())
				if b not in seen:
					seen.add(b)
					queue.append((b, moves+1))
					ml = True
					break
		if ml:
			continue
		for i in range(len(board)-1):
			if (board[i] and not board[i+1]) or (board[i] and board[i+1] and board[i][-1] < board[i+1][-1]):
				b = moveList([z[:] for z in board])
				b[i+1].append(b[i].pop())
				if b not in seen:
					seen.add(b)
					queue.append((b, moves+1))
		for i in range(1, len(board)):
			if (board[i] and not board[i-1]) or (board[i] and board[i-1] and board[i][-1] < board[i-1][-1]):
				b = moveList([z[:] for z in board])
				b[i-1].append(b[i].pop())
				if b not in seen:
					seen.add(b)
					queue.append((b, moves+1))

	if not win:
		print("IMPOSSIBLE")

	inp.pop(0)
	inp.pop(0)