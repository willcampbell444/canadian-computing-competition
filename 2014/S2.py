# CORRECT, PERFECT

with open("S2.in") as file:
    input = file.read().split("\n")

numOfPeople = int(input[0])
listOne = input[1].split(" ")
listTwo = input[2].split(" ")

partners = [(listOne[i], listTwo[i]) for i in range(numOfPeople)]

bad = False

for i in partners:
    if (i[1], i[0]) not in partners or i[0] == i[1]:
        bad = True
        break

if bad:
    print("bad")
else:
    print("good")