import hashlib

with open("day04.txt", "r") as f:
    inputString = f.readline()

number = 0
foundFirst = False
foundSecond = False

while True:
    encodeString = inputString + str(number)
    hashedString = hashlib.md5(encodeString.encode()).hexdigest()
    if hashedString.startswith('00000') and not foundFirst:
        print(number, encodeString, hashedString)
        foundFirst = True
    if hashedString.startswith('000000'):
        print(number, encodeString, hashedString)
        break

    number += 1
