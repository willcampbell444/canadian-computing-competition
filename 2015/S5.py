import random

with open("S5.in") as file:
    input = file.read().split()

N = int(input[0])
listOne = input[1:N+1]
listTwo = input[2+N:]
listTwo.sort()

print(listOne, listTwo)

# Random for testing
# nl = random.randint(1, 3000)
# listOne = [random.randint(1, 100000) for i in range(1, nl)]
# ml = random.randint(1, 100)
# listTwo = [random.randint(1, 100000) for i in range(1, ml)]
