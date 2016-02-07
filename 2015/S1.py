# PERFECT

with open("S1.in") as file:
    input = [int(i) for i in file.read().split()]

list = []

for i in input[1:]:
    if i == 0:
        list.pop()
    else:
        list.append(i)

print(sum(list))
