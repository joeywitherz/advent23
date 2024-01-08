import math


lines = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
]

file = open("input4.txt")
lines = file.readlines()

total = 0

for game in lines:
    cardNumber, content = game.split(":")
    elf, winning = content.split("|")

    #   - Sanitize
    elfNums = elf.strip().replace("  ", " ").split(" ")
    elfNums = set([int(x) for x in elfNums])

    winNums = winning.strip().replace("  ", " ").split(" ")
    winNums = set([int(x) for x in winNums])

    numOfWins = len(elfNums.intersection(winNums))

    if numOfWins > 0:
        total = total + math.pow(2, numOfWins-1)

    print(cardNumber)
    print(numOfWins)

print(total)
print(math.pow(2, -3))

# 2^-3 = 1/(2x2x2) = 1/8
# 2^-2 = 1/(2x2)   = 1/4
# 2^-1 = 1/2       = 1/2
# 2^0  = 1         = 1
# 2^1  = 2         = 2
# 2^2  = 2x2       = 4
# 2^3  = 2x2x2     = 8
