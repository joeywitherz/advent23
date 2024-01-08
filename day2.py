test1 = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
]


def isColorOkay(color):
    trimmed = color.strip()
    quantity, colorName = trimmed.split(" ")

    if colorName == "blue" and int(quantity) > 14:
        return False

    if colorName == "red" and int(quantity) > 12:
        return False

    if colorName == "green" and int(quantity) > 13:
        return False

    return True


def getColorName(color):
    trimmed = color.strip()
    _, colorName = trimmed.split(" ")

    return colorName


def getColorQuantity(color):
    trimmed = color.strip()
    quantity, _ = trimmed.split(" ")

    return int(quantity)


def isHandfulOkay(handful):
    colors = handful.split(",")
    return all([isColorOkay(color) for color in colors])


def part1():
    file = open("input2.txt")
    lines = file.readlines()

    total = 0
    for game in lines:
        # Destruction: take a string and splits it on the specificed char and shoves the parts into the defined variables
        gameDefinition, content = game.split(":")
        _, num = gameDefinition.split(" ")

        handfuls = content.split(";")
        gameOkay = all([isHandfulOkay(handful) for handful in handfuls])
        if gameOkay:
            total = total + int(num)
        else:
            total = total + 0

    print(total)


def part2():
    file = open("input2.txt")
    lines = file.readlines()

    total = 0
    for game in lines:
        _, content = game.split(":")
        colors = content.replace(";", ",").split(",")
        reds = max([getColorQuantity(color)
                   for color in colors if getColorName(color) == "red"])
        blues = max([getColorQuantity(color)
                    for color in colors if getColorName(color) == "blue"])
        greens = max([getColorQuantity(color)
                     for color in colors if getColorName(color) == "green"])

        total = total + (reds * greens * blues)

    print(total)


part2()
