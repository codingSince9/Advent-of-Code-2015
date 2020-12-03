strings = []
vowels = ['a', 'e', 'i', 'o', 'u']
forbiddenStrings = ['ab', 'cd', 'pq', 'xy']

f = open("day05.txt", "r")
for line in f:
    strings.append(line.strip())

niceStringCounter = 0

for niceString in strings:
    twoChars = ""
    vowelCounter = 0
    doubleLetter = False
    charCounter = 0
    for char in niceString:
        if len(twoChars) == 2:
            if twoChars[0] == twoChars[1]:
                doubleLetter = True
            if twoChars in forbiddenStrings:
                vowelCounter = 0
                doubleLetter = False
                break
            twoChars = twoChars[1]
        twoChars += char

        # last element check
        if charCounter == len(niceString)-1:
            if twoChars[0] == twoChars[1]:
                doubleLetter = True
            if twoChars in forbiddenStrings:
                vowelCounter = 0
                doubleLetter = False
                break

        if char in vowels:
            vowelCounter += 1

        charCounter += 1

    if vowelCounter >= 3 and doubleLetter:
        niceStringCounter += 1

# PART 1 ---------------
print(niceStringCounter)

niceStringCounter2 = 0

for niceString in strings:
    twoChars = ""
    threeCharCheck = ""
    separatedLetterCounter = False
    doubleLetterTwice = False
    charCounter = 0
    doubleLetterCheck = []
    for char in niceString:
        if len(twoChars) == 2:
            if twoChars in doubleLetterCheck and threeCharCheck != len(threeCharCheck) * threeCharCheck[0]:
                doubleLetterTwice = True
            else:
                doubleLetterCheck.append(twoChars)
            twoChars = twoChars[1]

        if len(threeCharCheck) == 3:
            threeCharCheck = threeCharCheck[1:]
        threeCharCheck += char
        twoChars += char

        # last element check
        if charCounter == len(niceString) - 1:
            if twoChars in doubleLetterCheck and threeCharCheck != len(threeCharCheck) * threeCharCheck[0]:
                doubleLetterTwice = True

        if len(threeCharCheck) == 3:
            if threeCharCheck[0] == threeCharCheck[2] and threeCharCheck[0] != threeCharCheck[1]:
                separatedLetterCounter = True

        charCounter += 1

    if separatedLetterCounter and doubleLetterTwice:
        niceStringCounter2 += 1

# PART 2 ----------------
print(niceStringCounter2)
