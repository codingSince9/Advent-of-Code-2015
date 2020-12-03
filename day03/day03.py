justSantaHouses = {str([0, 0]): 1}
roboAndSantaHouses = {str([0, 0]): 2}

with open("day03.txt", "r") as f:
    directions = f.readline()


def directionCount(direction, countUpDown, countRightLeft):
    if direction == '^':
        countUpDown += 1
    elif direction == 'v':
        countUpDown -= 1
    elif direction == '>':
        countRightLeft += 1
    else:
        countRightLeft -= 1

    return countUpDown, countRightLeft


def visitHouse(houses, direction, countUpDown, countRightLeft):
    coordinates = [countUpDown, countRightLeft]
    if str(coordinates) in houses.keys():
        houses[str(coordinates)] += 1
    else:
        houses[str(coordinates)] = 1

    return houses


def countHouses(houses):
    houseCounter = 0
    for visited in houses.values():
        if visited >= 1:
            houseCounter += 1

    print(houseCounter)


def partOne():
    countUpDown = 0
    countRightLeft = 0
    for direction in directions:
        countUpDown, countRightLeft = directionCount(direction, countUpDown, countRightLeft)
        justSantaHouses.update(visitHouse(justSantaHouses, direction, countUpDown, countRightLeft))

    countHouses(justSantaHouses)


def partTwo():
    santaCountUpDown = 0
    santaCountRightLeft = 0
    roboCountUpDown = 0
    roboCountRightLeft = 0
    santaTurn = True
    for direction in directions:
        if santaTurn:
            santaCountUpDown, santaCountRightLeft = directionCount(direction, santaCountUpDown, santaCountRightLeft)
            roboAndSantaHouses.update(visitHouse(roboAndSantaHouses, direction, santaCountUpDown, santaCountRightLeft))
            santaTurn = False
        else:
            roboCountUpDown, roboCountRightLeft = directionCount(direction, roboCountUpDown, roboCountRightLeft)
            roboAndSantaHouses.update(visitHouse(roboAndSantaHouses, direction, roboCountUpDown, roboCountRightLeft))
            santaTurn = True

    countHouses(roboAndSantaHouses)


partOne()
partTwo()
