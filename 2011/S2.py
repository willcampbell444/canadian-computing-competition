# PERFECT, 12 min

with open("S2.in") as file:
	inpu = file.read().strip().split('\n')

n = int(inpu[0])
inpu = inpu[1:]
responces = inpu[:n]
answers = inpu[n:]

correct = 0
for i in range(len(responces)):
	if responces[i] == answers[i]:
		correct += 1

print(correct)