import subprocess, os

problem = '2'

files = os.listdir("tests/senior/S"+problem+"/")
files.sort()
temp = []

count = 0
while count < len(files):
	temp.append([files[count], files[count+1]])
	count += 2

files = temp

for file in files:
	with open("tests/senior/S"+problem+"/"+file[0]) as doggy:
		with open("./S"+problem+".in", 'w') as cat:
			cat.write(doggy.read())

	print(" >>", file[0]+":")
	subprocess.call(["python", "./S"+problem+".py"])
	with open("tests/senior/S"+problem+"/"+file[1]) as horse:
		print("\n"+horse.read())