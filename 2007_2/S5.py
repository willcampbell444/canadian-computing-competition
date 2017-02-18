import sys

inp = sys.stdin.readlines()
inp.reverse()
inp.pop()

while inp:
	x = inp.pop().split()
	numPins = int(x[0])
	numBalls = int(x[1])
	width = int(x[2])

	pins = [int(inp.pop()) for _ in range(numPins)]
	if width*numBalls >= numPins:
		print(sum(pins))
	else:
		scores = []
		pos = width
		s = sum(pins[n] for n in range(width))
		scores.append(s)
		while pos < numPins:
			s -= pins[pos-width]
			s += pins[pos]
			pos += 1
			scores.append(s)
		previous = [0 for i in range(len(scores))]
		current = [0 for i in range(len(scores))]
		for b in range(numBalls):
			score = 0
			for i in range(len(current)):
				s = previous[i] + scores[b*width + i]
				if s > score:
					score = s
				current[i] = score
			previous = current
			current = [0 for i in range(len(previous)-width)]
		print(previous[-1])