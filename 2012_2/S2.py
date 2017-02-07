import sys

amn = sys.stdin.read().strip()

vals = {
	"I": 1,
	"V": 5,
	"X": 10,
	"L": 50,
	"C": 100,
	"D": 500,
	"M": 1000
}

val = 0

for i in range(0, len(amn)-2, 2):
	if vals[amn[i+1]] < vals[amn[i+3]]:
		val -= int(amn[i]) * vals[amn[i+1]]
	else:
		val += int(amn[i]) * vals[amn[i+1]]

val += int(amn[-2]) * vals[amn[-1]]

print(val)