with open("S3.in") as file:
    input = [int(i) for i in file.read().split("\n")]

gates = [False for i in range(input[0])]
planes = input[2:]

landed = 0

for target in planes:
    stopped = True
    for i in reversed(range(target)):
        if not gates[i]:
            gates[i] = True
            stopped = False
            landed += 1
            break
    if stopped:
        break

print(landed)