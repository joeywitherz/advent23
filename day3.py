lines = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
    ".........."]


def isSymbol(char):
    return char != '.' and char.isnumeric() == False


def hasAdjacentSymbol(grid, x, y):
    return (
        isSymbol(grid[y-1][x-1]) or isSymbol(grid[y][x-1]) or isSymbol(grid[y+1][x-1]) or
        isSymbol(grid[y-1][x]) or isSymbol(grid[y+1][x]) or
        isSymbol(grid[y-1][x+1]) or isSymbol(grid[y][x+1]) or
        isSymbol(grid[y+1][x+1])
    )


def wholeNumHasAdjacentSymbol(grid, x, y, length):
    hits = [hasAdjacentSymbol(grid, x - coord, y)
            for coord in range(0, length)]

    return any(hits)


file = open("input3.txt")
lines = file.readlines()

lines = list(map(lambda x: "." + x.strip() + ".", lines))

grid = [list(str) for str in lines]
total = 0
accum = ""
for yIndex, row in enumerate(lines):  # go through each row (line) of the grid
    # and of that, go through each col (char) of the row
    for xIndex, char in enumerate(row):
        if char.isnumeric():
            accum = accum + char

        if char.isnumeric() == False and len(accum) > 0:
            # minus one to move us back into the territory of the number part of the string
            if wholeNumHasAdjacentSymbol(grid, xIndex-1, yIndex, len(accum)):
                total = total + int(accum)

            accum = ""

print(total)
