# This one took me a long time for some reason

with open("S3.in") as file:
	inpu = file.read().split('\n')

team = int(inpu[0])-1
games = [[int(j)-1 for j in i.split()] for i in inpu[2:]]
teams = [0 for i in range(4)]
matchups = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]

def playGame(penis, a, b, outcome):
	leScore = [i for i in penis]
	if outcome == 0:
		leScore[a] += 3
	elif outcome == 1:
		leScore[b] += 3
	elif outcome == 2:
		leScore[a] += 1
		leScore[b] += 1

	return leScore


for i in games:
	matchups.remove(i[:2])

	if i[2] > i[3]:
		teams[i[0]] += 3
	elif i[3] > i[2]:
		teams[i[1]] += 3
	elif i[2] == i[3]:
		teams[i[0]] += 1
		teams[i[1]] += 1

possibleScores = [[teams]]

for i in range(len(matchups)):
	possibleScores.append([])
	for score in possibleScores[i]:
		for w in range(3):
			possibleScores[i+1].append(playGame(score, matchups[i][0], matchups[i][1], w))

wins = 0
for i in possibleScores[-1]:
	if max(i) == i[team]:
		wins += 1

print(wins)