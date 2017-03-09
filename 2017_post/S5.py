import sys

inp = sys.stdin.readlines()

x = [int(i) for i in inp.pop(0).split()]

num_stations = x[0]
num_lines = x[1]

lines = [[] for i in range(num_lines)]
rotations = [0 for i in range(num_lines)]

station_line = [[int(i)-1, -1] for i in inp.pop(0).split()]
for x in range(num_stations):
	n = int(station_line[x][0])
	station_line[x][1] = len(lines[n-1])
	lines[n-1].append(x)

populations = [int(i) for i in inp.pop(0).split()]
sums = [0, populations[0]]
for i in range(1, len(populations)):
	sums.append(populations[i]+sums[i])

summed = True
for action in inp:
	action = action.split()

	if action[0] == '1':
		if summed:
			print(sums[int(action[2])] - sums[int(action[1])-1])
		else:
			sums[1] = populations[0]
			for i in range(1, len(populations)):
				print()
				sums[i+1] = sums[i]+populations[lines[station_line[i][0]][(station_line[i][0]+rotations[station_line[i][0]])%len(lines[station_line[i][0]])]]
			summed = True
			print(sums[int(action[2])] - sums[int(action[1])-1])
	else:
		summed = False