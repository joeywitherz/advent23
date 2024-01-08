mode = "live"

if mode == "live":
    file = open("input5_seeds.txt")
    seeds = file.readlines()[0]

    file = open("input5_seed-to-soil.txt")
    seedToSoil = file.readlines()

    file = open("input5_soil-to-fertilizer.txt")
    soilToFertilzer = file.readlines()

    file = open("input5_fertilizer-to-water.txt")
    fertilzerToWater = file.readlines()

    file = open("input5_water-to-light.txt")
    waterToLight = file.readlines()

    file = open("input5_light-to-temperature.txt")
    lightToTemperature = file.readlines()

    file = open("input5_temperature-to-humidity.txt")
    temperatureToHumidity = file.readlines()

    file = open("input5_humidity-to-location.txt")
    humidityToLocation = file.readlines()


if mode == "test":
    seeds = "79 14 55 13"

    seedToSoil = ["50 98 2",
                  "52 50 48"]

    soilToFertilzer = ["0 15 37",
                       "37 52 2",
                       "39 0 15"]

    fertilzerToWater = ["49 53 8",
                        "0 11 42",
                        "42 0 7",
                        "57 7 4"]

    waterToLight = ["88 18 7",
                    "18 25 70"]

    lightToTemperature = ["45 77 23",
                          "81 45 19",
                          "68 64 13"]

    temperatureToHumidity = ["0 69 1",
                             "1 0 69",]

    humidityToLocation = ["60 56 37",
                          "56 93 4"]


def splitSectionCovertInt(section: list[str]):
    return [[int(y) for y in x.split(" ")] for x in section]


seedList = [int(x) for x in seeds.split(" ")]


def mapSection(section, number):
    mappings = splitSectionCovertInt(section)
    i = 0
    result = 0
    while result == 0 and i < len(mappings):
        destination, source, range = mappings[i]
        highestRangeSource = range + source
        if number >= source and number <= highestRangeSource:
            result = destination - source + number
        i = i + 1

    if result == 0:
        return number
    return result


def seedToLocation(seed):
    soil = mapSection(seedToSoil, seed)
    fert = mapSection(soilToFertilzer, soil)
    water = mapSection(fertilzerToWater, fert)
    light = mapSection(waterToLight, water)
    temp = mapSection(lightToTemperature, light)
    hum = mapSection(temperatureToHumidity, temp)
    loc = mapSection(humidityToLocation, hum)

    return loc


def getLowestSeedLocation():
    minimum = float('inf')

    for seed in seedList:
        loc = seedToLocation(seed)
        if loc < minimum:
            minimum = loc

    print(minimum)


def getLowestSeedLocationComp():
    locations = [seedToLocation(seed) for seed in seedList]
    print(min(locations))


getLowestSeedLocation()
getLowestSeedLocationComp()
