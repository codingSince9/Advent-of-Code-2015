instructions = []
lights = {}
lightsBrightness = {}
lightCounter = 0
totalBrightness = 0

f = open("day06.txt", "r")
for line in f:
    instructions.append(line.strip())

for i in range(1000):
    for j in range(1000):
        location = str(i) + ',' + str(j)
        lights[location] = False
        lightsBrightness[location] = 0


def electrician(start, end, turnOnOff, toggleLight):
    for i in range(int(start.split(',')[0]), int(end.split(',')[0]) + 1):
        for j in range(int(start.split(',')[1]), int(end.split(',')[1]) + 1):
            lightLocation = str(i) + ',' + str(j)
            if turnOnOff and not toggleLight:
                lights[lightLocation] = True
                lightsBrightness[lightLocation] += 1
            elif not turnOnOff and not toggleLight:
                lights[lightLocation] = False
                if lightsBrightness[lightLocation] != 0:
                    lightsBrightness[lightLocation] -= 1
            else:
                lights[lightLocation] = not lights[lightLocation]
                lightsBrightness[lightLocation] += 2


for instruction in instructions:
    toggle = True
    instruction = instruction.split()

    if len(instruction) == 5:
        lightStart = instruction[2]
        toggle = False
    else:
        lightStart = instruction[1]
    lightEnd = instruction[-1]

    if instruction[1] == 'on':
        electrician(lightStart, lightEnd, True, toggle)
    elif instruction[1] == 'off':
        electrician(lightStart, lightEnd, False, toggle)
    else:
        electrician(lightStart, lightEnd, False, toggle)

for i in range(1000):
    for j in range(1000):
        location = str(i) + ',' + str(j)
        if lights[location]:
            lightCounter += 1
        totalBrightness += lightsBrightness[location]

print("Part 1:", lightCounter)
print("Part 2:", totalBrightness)
