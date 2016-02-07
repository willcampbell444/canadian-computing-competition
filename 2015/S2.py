# Does not really work

with open("S2.in") as file:
    input = file.read().split("\n")

jerseys = int(input[0])
sizes = input[2:2+jerseys]
requests = input[2+jerseys:]

avalible = [
    sum(1 for i in sizes if i == "S"),
    sum(1 for i in sizes if i == "M"),
    sum(1 for i in sizes if i == "L")
]

numbersUsed = []
satisfied = 0

for i in requests:
    i = i.split()
    if i[1] not in numbersUsed:
        if i[0] == "S":
            if avalible[0] > 0:
                satisfied += 1
                numbersUsed.append(i[1])
                avalible[0] -= 1
            elif avalible[1] > 0:
                satisfied += 1
                numbersUsed.append(i[1])
                avalible[1] -= 1
            elif avalible[2] > 0:
                satisfied += 1
                numbersUsed.append(i[1])
                avalible[2] -= 1
        elif i[0] == "M":
            if avalible[1] > 0:
                satisfied += 1
                numbersUsed.append(i[1])
                avalible[1] -= 1
            elif avalible[2] > 0:
                satisfied += 1
                numbersUsed.append(i[1])
                avalible[2] -= 1
        elif i[0] == "L":
            if avalible[2] > 0:
                satisfied += 1
                numbersUsed.append(i[1])
                avalible[2] -= 1

print(satisfied)