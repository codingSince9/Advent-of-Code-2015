line = open("day10.txt", "r").readline()


def day10(iterate, sequence):
    for i in range(iterate):
        concat = ""
        first = True
        second = False
        sameNumberCounter = 0
        secondNum = 0
        numCounter = 0
        for num in sequence:
            numCounter += 1
            if second and secondNum != num:
                concat += str(sameNumberCounter) + str(secondNum)
                first = True
                second = False
                if numCounter == len(sequence):
                    sameNumberCounter = 1
                    concat += str(sameNumberCounter) + str(num)
                sameNumberCounter = 0
                secondNum = 0
            elif secondNum == num:
                sameNumberCounter += 1
                continue
            if first:
                firstNum = num
                sameNumberCounter += 1
                first = False
                continue
            elif firstNum == num:
                sameNumberCounter += 1
                continue
            else:
                concat += str(sameNumberCounter) + str(firstNum)
                secondNum = num
                second = True
                sameNumberCounter = 1
                if numCounter == len(sequence):
                    concat += str(sameNumberCounter) + str(secondNum)
        sequence = concat

    print(len(concat))


print("Part 1:")
day10(40, line)
print("Part 2:")
day10(50, line)

