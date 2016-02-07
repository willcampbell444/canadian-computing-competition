# CORRECT, PERFECT

with open("S3.in") as file:
    inp = [int(i) for i in file.readlines()]

list = []

for i in range(inp[0]):
    list.append(inp[2:inp[1]+2])
    inp = inp[inp[1]+1:]

def test(cars):
    top = cars
    branch = []

    for i in range(1, len(cars)+1):
        cycleNotDone = True
        while cycleNotDone:
            if top and top[-1] == i:
                top.pop()
                cycleNotDone = False
            elif branch and branch[-1] == i:
                branch.pop()
                cycleNotDone = False
            elif top:
                branch.append(top.pop())
            else:
                print("N")
                return
    print("Y")

for i in list:
    test(i)