import sys
from collections import deque

inp = sys.stdin.readlines()

lights = deque([int(x) for x in inp[1:]])

while len(lights) > 4 and lights[0] == 0:
	lights.popleft()

while len(lights) > 4 and lights[-1] == 0:
	lights.pop()

class lightList(list):
	def __hash__(self):
		l = len(self)-1
		total = 0
		for i in self:
			total += i*2**l
			l -= 1
		return total

newLights = lightList()
s = 0
while lights:
	x = lights.popleft()
	if x != 0:
		s += x
	elif s != 0:
		newLights.append(s)
		s = 0
		newLights.append(0)
	else:
		newLights.append(0)
if s:
	newLights.append(s)

beenDone = set()
beenDone.add(newLights)
actions = deque([(newLights, 0)])

while actions:
	action, mcount = actions.popleft()

	if sum(action) == 0:
		print(mcount)
		break

	for i in range(len(action)):
		if action[i] == 0:
			if i > 0 and action[i-1]:
				l = action[i-1]+1
				li = i-1
			else:
				l = 1
				li = i

			if i < len(action)-1 and action[i+1]:
				l += action[i+1]
				ri = i+2
			else:
				ri = i+1
			if l >= 4:
				# search left and right?
				nl = lightList(action[:li]+[0, 0, 0, 0]+action[ri:])
			else:
				nl = lightList(action[:li]+[l]+action[ri:])
			if nl not in beenDone:
				beenDone.add(nl)
				actions.append((nl, mcount+1))

# WIP FASTER

# import sys
# from collections import deque

# inp = sys.stdin.readlines()

# lights = deque([int(x) for x in inp[1:]])

# while len(lights) > 4 and lights[0] == 0:
# 	lights.popleft()

# while len(lights) > 4 and lights[-1] == 0:
# 	lights.pop()

# lights = list(lights)

# llights = []
# sst = 0
# zst = -1
# lenzero = 0
# for i in range(len(lights)):
# 	if lights[i] == 0:
# 		if zst < 0:
# 			zst = i
# 		lenzero += 1
# 	else:
# 		if lenzero > 4:
# 			llights.append(lights[sst:zst])
# 			sst = i
# 		zst = -1
# 		lenzero = 0
# llights.append(lights[sst:])

# class lightList(list):
# 	def __hash__(self):
# 		l = len(self)-1
# 		total = 0
# 		for i in self:
# 			total += i*2**l
# 			l -= 1
# 		return total
# 	def length(self):
# 		l = 0
# 		for i in self:
# 			if i == 0:
# 				l += 1
# 			else:
# 				l += i
# 		return i

# def count(lights):
# 	lights = deque(lights)

# 	if len(lights) <= 4:
# 		return 4-sum(lights)

# 	newLights = lightList()
# 	s = 0
# 	while lights:
# 		x = lights.popleft()
# 		if x != 0:
# 			s += x
# 		elif s != 0:
# 			newLights.append(s)
# 			s = 0
# 			newLights.append(0)
# 		else:
# 			newLights.append(0)
# 	if s:
# 		newLights.append(s)

# 	beenDone = set()
# 	beenDone.add(newLights)
# 	actions = deque([(newLights, 0)])

# 	while actions:
# 		action, mcount = actions.popleft()

# 		for i in range(len(action)):
# 			if action[i] == 0:
# 				if i > 0 and action[i-1]:
# 					l = action[i-1]+1
# 					li = i-1
# 				else:
# 					l = 1
# 					li = i

# 				if i < len(action)-1 and action[i+1]:
# 					l += action[i+1]
# 					ri = i+2
# 				else:
# 					ri = i+1
# 				if l >= 4:
# 					# search left and right?
# 					nl = lightList(action[:li]+[0, 0, 0, 0]+action[ri:])
# 				else:
# 					nl = lightList(action[:li]+[l]+action[ri:])
# 				if sum(nl) == 0:
# 					return mcount+1
# 				if nl not in beenDone:
# 					beenDone.add(nl)
# 					actions.append((nl, mcount+1))

# print(sum(count(i) for i in llights))