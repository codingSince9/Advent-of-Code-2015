floor = 0
charPosition = 0
counter = 0
basement = False

with open("day01.txt", "r") as f:
    line = f.readline()

for char in line:
    if char == '(':
        floor += 1
    else:
        floor -= 1

    counter += 1

    if floor == -1 and not basement:
        charPosition = counter
        basement = True

print(floor)
print(charPosition)