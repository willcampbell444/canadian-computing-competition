import subprocess, os
from timeit import default_timer

problem = 'troyangles'
filePath = ""

files = os.listdir(filePath+problem+"/")
files.sort()
temp = []

count = 0
while count < len(files):
	temp.append([files[count], files[count+1]])
	count += 2

files = temp

for file in files:
	with open(filePath+problem+"/"+file[0]) as doggy:
		with open("./"+problem+".in", 'w') as cat:
			cat.write(doggy.read())

	print(" >>", file[0]+":")
	t = default_timer()
	subprocess.call(["python", "./"+problem+".py"])
	print("TIME ELAPSED:", str(round(default_timer()-t, 2)))
	with open(filePath+problem+"/"+file[1]) as horse:
		print("\n"+horse.read())