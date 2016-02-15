# FAILURE

import sys

# with open("S4.in") as file:
# 	inpu = file.read().strip().split('\n')


inpu = sys.stdin.read().strip().split('\n')

pens = [[int(j) for j in i.split()] for i in inpu[1:]]

cost = 0

single = []

def edges(a):
	e = []
	corners = pens[a][1:pens[a][0]+1]
	costs = pens[a][pens[a][0]+1:]
	for i in range(-1, len(corners)-1):
		e.append([corners[i], corners[i+1], costs[i]])
		if [corners[i], corners[i+1], costs[i]] in pens[a] or [corners[i+1], corners[i], costs[i]] in pens[a]:
			single.pop(e)
		else: 
			single.append(e)
	return e

pens = [edges(i) for i in range(len(pens))]

def merge(a, b):
	connections = []
	for i in pens[a]:
		if i in pens[b]:
			connections.append(i)
		elif [i[1], i[0], i[2]] in pens[b]:
			connections.append(i)
	cheapest = connections[0]
	for c in connections:
		if c[2] < cheapest[2]:
			cheapest = c
	for c in connections:
		pens[a].remove(c)
		if c in pens[b]:
			pens[b].remove(c)
		elif [c[1], c[0], c[2]] in pens[b]:
			pens[b].remove([c[1], c[0], c[2]])
	newPen = pens[a] + pens[b]
	if b > a:
		pens.pop(b)
		pens.pop(a)
	else:
		pens.pop(a)
		pens.pop(b)
	pens.append(newPen)
	return cheapest[2]

def connected(a, b):
	for i in pens[a]:
		if i in pens[b]:
			return True
		elif [i[1], i[0], i[2]] in pens[b]:
			return True
	return False

def costOfMerge(a, b):
	connections = []
	for i in pens[a]:
		if i in pens[b]:
			connections.append(i)
		elif [i[1], i[0], i[2]] in pens[b]:
			connections.append(i)
	cheapest = connections[0]
	for c in connections:
		if c[2] < cheapest[2]:
			cheapest = c
	return cheapest[2]


while len(pens) > 1:
	cheapest = -1
	aa = 0
	bb = 0
	# Delete cheepest
	for i in range(len(pens)):
		for j in range(len(pens)):
			if i != j and connected(i, j):
				price = costOfMerge(i, j)
				if cheapest == -1 or price < cheapest:
					cheapest = price
					aa = i
					bb = j
	cost += cheapest
	merge(aa, bb)

print(cost)