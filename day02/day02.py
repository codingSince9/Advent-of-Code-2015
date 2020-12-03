presents = []
totalFeet = 0
feetOfRibbon = 0

f = open("day02.txt", "r")
for line in f:
    presents.append(line.strip())

print(presents)
for present in presents:
    dimensions = [int(x) for x in present.split('x')]
    dimensions.sort()
    smallestSide = dimensions[0] * dimensions[1]
    feetOfRibbon += 2*(dimensions[0] + dimensions[1]) + dimensions[0] * dimensions[1] * dimensions[2]
    totalFeet += 2 * dimensions[0] * dimensions[1] + 2 * dimensions[1] * dimensions[2] + 2 * dimensions[0] * dimensions[2] + smallestSide

print(totalFeet)
print(feetOfRibbon)
