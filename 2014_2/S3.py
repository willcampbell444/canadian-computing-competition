import sys

inpu = sys.stdin.read().strip()

data = [int(i) for i in inpu.split('\n')] # convert the input into a list of integers
data.reverse() # reverse it so we can pop from the back easily

for _ in range(data.pop()): # will run once for each test case
	num_cars = data.pop() # get the number of cars

	# make a list of the cars that start on the mountain top
	mountainTop = []
	for _ in range(num_cars):
		mountainTop.append(data.pop())

	branch = [] # for storing the cars on the branch
	toBottom = 1 # the nect car that needs to reach the bottom

	# will run while there are cars remaining
	while mountainTop or branch:
		# if the next car that needs to exit is at the front of the mountain top train, send it down
		if mountainTop and mountainTop[-1] == toBottom:
			mountainTop.pop()
			toBottom += 1
		# or else if the next cat that needs to exit is at the front of the branch, send it down
		elif branch and branch[-1] == toBottom:
			branch.pop()
			toBottom += 1
		# or else if there are still cars remaining on the mountain top, push one to the front of the branch
		elif mountainTop:
			branch.append(mountainTop.pop())
		# it is unsolvable, so stop
		else:
			break

	# if there are still cars on the branch it is unsolvable
	if branch:
		print("N")
	else:
		print("Y")