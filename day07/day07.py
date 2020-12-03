instructions = []
sortedInstructions = []
wireSignals = {}

f = open("day07.txt", "r")
for line in f:
    instructions.append(line.strip())


def checkIfNum(number):
    try:
        int(number)
        return True
    except ValueError:
        return False


def run():
    for instruction in sortedInstructions:
        if len(instruction.split()) == 5:
            firstVariable = instruction.split()[0]
            secondVariable = instruction.split()[2]
            firstIsNum = checkIfNum(firstVariable)
            secondIsNum = checkIfNum(secondVariable)

            if firstIsNum and secondIsNum:
                firstInt = int(firstVariable)
                secondInt = int(secondVariable)
            elif firstIsNum and not secondIsNum:
                firstInt = int(firstVariable)
                secondInt = wireSignals[secondVariable]
            elif not firstIsNum and secondIsNum:
                firstInt = wireSignals[firstVariable]
                secondInt = int(secondVariable)
            else:
                firstInt = wireSignals[firstVariable]
                secondInt = wireSignals[secondVariable]

            if instruction.split()[1] == 'AND':
                number = firstInt & secondInt
            if instruction.split()[1] == 'OR':
                number = firstInt | secondInt
            if instruction.split()[1] == 'RSHIFT':
                number = firstInt >> secondInt
            if instruction.split()[1] == 'LSHIFT':
                number = firstInt << secondInt

            wireSignals[instruction.split()[-1]] = number

        if len(instruction.split()) == 4:
            firstVariable = instruction.split()[1]
            firstIsNum = checkIfNum(firstVariable)
            if firstIsNum:
                firstInt = int(firstVariable)
            else:
                firstInt = wireSignals[firstVariable]
            wireSignals[instruction.split()[-1]] = ~firstInt if ~firstInt > 0 else 65536 + ~firstInt

        if len(instruction.split()) == 3:
            if checkIfNum(instruction.split()[0]):
                wireSignals[instruction.split()[2]] = int(instruction.split()[0])
            else:
                wireSignals[instruction.split()[2]] = wireSignals[instruction.split()[0]]


while len(instructions) != 0:
    for instruction in instructions:
        if len(instruction.split()) == 5:
            firstAvailable = checkIfNum(instruction.split()[0])
            secondAvailable = checkIfNum(instruction.split()[2])

            for ins in sortedInstructions:
                if ins.split()[-1] == instruction.split()[0] and not firstAvailable:
                    firstAvailable = True
                if ins.split()[-1] == instruction.split()[2] and not secondAvailable:
                    secondAvailable = True
                if firstAvailable and secondAvailable:
                    sortedInstructions.append(instruction)
                    instructions.remove(instruction)
                    break

        if len(instruction.split()) == 4:
            for ins in sortedInstructions:
                if ins.split()[-1] == instruction.split()[1]:
                    sortedInstructions.append(instruction)
                    instructions.remove(instruction)
                    break

        if len(instruction.split()) == 3:
            if checkIfNum(instruction.split()[0]):
                sortedInstructions.append(instruction)
                instructions.remove(instruction)
            else:
                for ins in sortedInstructions:
                    if instruction.split()[0] == ins.split()[-1]:
                        sortedInstructions.append(instruction)
                        instructions.remove(instruction)
                        break

run()
print("Part 1:", wireSignals['a'])

newB = str(wireSignals['a']) + ' -> b'
counter = 0
for instruction in sortedInstructions:
    if instruction.endswith('-> b'):
        sortedInstructions[counter] = newB
        break

run()
print("Part 2:", wireSignals['a'])
