import subprocess, os

problem = '5'

files = os.listdir("tests/s"+problem+"/")
files.sort()
temp = []

count = 0
while count < len(files):
	temp.append([files[count], files[count+1]])
	count += 2

files = temp

for file in files:
	with open("tests/s"+problem+"/"+file[0]) as doggy:
		with open("./S"+problem+".in", 'w') as cat:
			cat.write(doggy.read())

	with open("tests/s"+problem+"/"+file[1]) as horse:
		print(" >>", file[0]+":")
		subprocess.call(["python", "./S"+problem+".py"])
		print("\n"+horse.read())