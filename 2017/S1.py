import sys

inp = sys.stdin.readlines()

inp.pop(0)

sem = [int(i) for i in inp[0].split()]
swif = [int(i) for i in inp[1].split()]

semtot = 0
swiftot = 0

samei = 0

for i in range(len(sem)):
	semtot += sem[i]
	swiftot += swif[i]
	if semtot == swiftot:
		samei = i+1
print(samei)