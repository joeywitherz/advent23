test1 = [
    "1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"
]

test2 = [
    "two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"
]


def replaceWrittenNumbers(str):
    return (
        str.replace("one", "o1e")
        .replace("two", "t2o")
        .replace("three", "t3e")
        .replace("four", "f4r")
        .replace("five", "f5e")
        .replace("six", "s6x")
        .replace("seven", "s7n")
        .replace("eight", "e8t")
        .replace("nine", "n9e")
    )


def isnum(str):
    return str.isnumeric()


def extractCode(characters):
    numbers = list(filter(isnum, characters))

    return int(numbers[0] + numbers[- 1])


def convertThenExtractCode(line):
    line = replaceWrittenNumbers(line)

    return extractCode(line)


def process(mappingFunction):
    file = open("input1.txt")
    lines = file.readlines()

    codes = map(mappingFunction, lines)
    total = sum(codes)

    print(total)


process(extractCode)
process(convertThenExtractCode)
