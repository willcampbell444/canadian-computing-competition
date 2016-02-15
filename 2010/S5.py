# Works nicely, but too slow

import sys

# with open("S5.in") as file:
	# inpu = file.read().strip().split('\n')
inpu = sys.stdin.read().strip().split('\n')

class Node():
	def __init__(self, value):
		self.r = None
		self.l = None
		self.val = value

tree = inpu[0]
growth = int(inpu[1])

root = None

def fillTree(str, node):
	str = str.strip()
	node = Node(False)
	if str == '':
		return None
	elif str[0] != '(':
		node.val = int(str)
		return node
	else:
		str = str[1:-1]
		str = str.strip()
		i = str.find('(')
		if i == -1:
			str = str.split()
			node.l = fillTree(str[0], node.l)
			node.r = fillTree(str[1], node.r)
			return node
		else:
			o = 0
			for s in range(len(str)):
				if str[s] == '(':
					o += 1
				elif str[s] == ')':
					o -= 1
				elif o == 0 and str[s] == ' ':
					i = s
					break
			node.l = fillTree(str[:i].strip(), node.l)
			node.r = fillTree(str[i:].strip(), node.r)
			return node

def printTree(node, depth):
	if node != None:
		printTree(node.l, depth+1)
		print('>>>'*depth, node.val)
		printTree(node.r, depth+1)

def count(node, max):
	if node != None:
		printTree(node.l, depth+1)
		if node.val:
			print('>>>'*depth, node.val)
		else:
			print('>>>'*depth)
		printTree(node.r, depth+1)

# def momom(node, possibilities):
# 	if node.l == None and node.r == None:
# 		for i in range(len(possibilities)):
# 			possibilities[i] = node.val+i
# 		return possibilities
# 	else:
# 		pl = momom(node.l, possibilities[:])
# 		pr = momom(node.r, possibilities[:])

# 		for i in range(len(possibilities)):
# 			top = 0
# 			for l in range(i+1):
# 				for r in range(i-l+1):
# 					for ppl in range(i-l-r+1):
# 						for ppr in range(i-l-r-ppl+1):
# 							n = 0
# 							ppll = (1+ppl)**2
# 							pprl = (1+ppr)**2
# 							if ppll >= pl[l]:
# 								n += pl[l]
# 							else:
# 								n += ppll
# 							if pprl >= pr[r]:
# 								n += pr[r]
# 							else:
# 								n += pprl

# 							if n > top:
# 								top = n
# 			possibilities[i] = top
# 		return possibilities

def momom(node, possibilities):
	if node.l == None and node.r == None:
		for i in range(len(possibilities)):
			possibilities[i] = node.val+i
		return possibilities
	else:
		pl = momom(node.l, possibilities[:])
		pr = momom(node.r, possibilities[:])

		optL = possibilities[:]
		optR = possibilities[:]

		for i in range(len(possibilities)):
			top = 0
			for j in range(i+1):
				t = min((1+j)**2, pl[i-j])
				if t > top:
					top = t
			optL[i] = top

		for i in range(len(possibilities)):
			top = 0
			for j in range(i+1):
				t = min((1+j)**2, pr[i-j])
				if t > top:
					top = t
			optR[i] = top

		for i in range(len(possibilities)):
			top = 0
			for j in range(i+1):
				t = optL[j] + optR[i-j]
				if t > top:
					top = t
			possibilities[i] = top

		return possibilities

root = fillTree(tree, root)
p = [0 for i in range(growth+1)]
print(max(momom(root, p)))