password = open("day11.txt", "r").readline().strip()


def increment(pwd):
    counter = 0
    pwd = ''.join(reversed(pwd))
    pwdList = list(pwd)
    for char in pwd:
        if chr(ord(char) + 1).isalpha():
            pwdList[counter] = chr(ord(char) + 1)
            break
        else:
            pwdList[counter] = 'a'
        counter += 1

    pwd = ''.join(pwdList)
    pwd = ''.join(reversed(pwd))

    return pwd


letterPairs = []
secondPart = False
while True:
    twoSameChars = ""
    doubleLetter = 0
    increasingThree = ""
    three = False
    forbiddenLetter = False
    letterPairs.clear()

    for char in password:
        if len(increasingThree) == 0:
            increasingThree += char
        elif len(increasingThree) == 1 and ord(increasingThree) + 1 == ord(char):
            increasingThree += char
        elif len(increasingThree) == 2 and ord(increasingThree[1]) + 1 == ord(char):
            increasingThree += char
            three = True
        elif increasingThree != char:
            increasingThree = ""

        if char == 'i' or char == 'o' or char == 'l':
            forbiddenLetter = True

        if len(twoSameChars) == 0:
            twoSameChars = char
            continue
        elif len(twoSameChars) == 1:
            if char == twoSameChars:
                twoSameChars += char
                if twoSameChars not in letterPairs:
                    doubleLetter += 1
                    letterPairs.append(twoSameChars)
            twoSameChars = char

    if three and not forbiddenLetter and doubleLetter >= 2 and not secondPart:
        print("Part 1:", password)
        passwordList = list(password)
        password = increment(password)
        secondPart = True
        continue
    if secondPart and three and not forbiddenLetter and doubleLetter >= 2:
        print("Part 2:", password)
        break

    counter = 0
    passwordList = list(password)

    # if i, o, l, then change letters after them to 'a'
    for char in password:
        if char == 'i' or char == 'o' or char == 'l':
            passwordList[counter] = chr(ord(char) + 1)
            for i in range(counter + 1, len(passwordList)):
                passwordList[i] = 'a'
            break
        counter += 1

    password = ''.join(passwordList)

    password = increment(password)
