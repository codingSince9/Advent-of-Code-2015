strings = []
hexCheck = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
codeCounter = 0
charCounter = 0
encodeCounter = 0

f = open("day08.txt", "r")
for string in f:
    strings.append(string.strip())

for string in strings:
    first = False
    x = False
    threeChars = ""
    for char in string:
        codeCounter += 1
        if char != '"':
            charCounter += 1

        if char == '\\' and not first:
            first = True
            x = False
            continue
        if char == '\\' and first:
            charCounter -= 1
            first = False
            continue
        if char == '"' and first:
            first = False
            continue
        if first or x:
            if char != 'x' and not x:
                charCounter -= 1
                first = False
                threeChars = ""
                continue
            else:
                if not x:
                    threeChars += char
                    x = True
                    continue
                if len(threeChars) < 3:
                    if char in hexCheck:
                        threeChars += char
                    else:
                        charCounter -= 1
                        threeChars = ""
                    if len(threeChars) == 3:
                        charCounter -= 3
                        first = False
                        x = False
                        threeChars = ""
                    continue

print("Part 1:", codeCounter - charCounter)

for string in strings:
    encodeCounter += 2
    for char in string:
        if char != '\\' and char != '"':
            encodeCounter += 1
        else:
            encodeCounter += 2

print("Part 2:", encodeCounter - codeCounter)
