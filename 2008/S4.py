# 7:15 - 3/15 (SUPER bad)

with open("S4.in") as file:
	inpu = file.read().strip().split('\n')

hands = int(inpu.pop(0))
games = []

for i in range(hands):
	games.append([int(i) for i in inpu[i*4:(i+1)*4]])

for g in games:
	maxx = 0
	for c1 in g:
		tmpg = g[:]
		tmpg.remove(c1)
		for c2 in tmpg:
			tmpg.remove(c2)
			for c3 in tmpg:
				tmpg.remove(c3)
				for c4 in tmpg:
					tmpg.remove(c4)

					n = c1+c2+c3+c4
					if n < 25 and n > maxx:
						maxx = n

					n = c1+c2+c3-c4
					if n < 25 and n > maxx:
						maxx = n

					n = c1+c2-c3-c4
					if n < 25 and n > maxx:
						maxx = n

					n = c1-c2-c3-c4
					if n < 25 and n > maxx:
						maxx = n

					n = (c1-c2-c3)*c4
					if n < 25 and n > maxx:
						maxx = n

					n = (c1-c2)*c4+c3
					if n < 25 and n > maxx:
						maxx = n

					n = (c1-c2)*(c4-c3)
					if n < 25 and n > maxx:
						maxx = n

					n = (c1-c2)*(c4+c3)
					if n < 25 and n > maxx:
						maxx = n

					n = (c1+c2)*(c4-c3)
					if n < 25 and n > maxx:
						maxx = n

					n = (c1+c2)*(c4+c3)
					if n < 25 and n > maxx:
						maxx = n

					n = ((c1*c2)-c3)*c4
					if n < 25 and n > maxx:
						maxx = n

					n = ((c1-c2)*c3)*c4
					if n < 25 and n > maxx:
						maxx = n

					n = ((c1*c2)-c3)-c4
					if n < 25 and n > maxx:
						maxx = n

					n = ((c1*c2)-c3)+c4
					if n < 25 and n > maxx:
						maxx = n

					n = ((c1*c2)+c3)-c4
					if n < 25 and n > maxx:
						maxx = n

					n = ((c1*c2)+c3)+c4
					if n < 25 and n > maxx:
						maxx = n

					n = ((c1+c2)+c3)+c4
					if n < 25 and n > maxx:
						maxx = n

					n = c1*c2*c3*c4
					if n < 25 and n > maxx:
						maxx = n

					n = (c1*c2*c3)/c4
					if n < 25 and n > maxx:
						maxx = n

					n = (c1*c2)/c3*c4
					if n < 25 and n > maxx:
						maxx = n
	print(maxx)