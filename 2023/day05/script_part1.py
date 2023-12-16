import re

input_file = 'example_part1.txt'
# input_file = 'puzzle_input.txt'

# Read the file
with open(input_file) as f:
    data = f.read()


def createMap(raw_map):
    p_convert_map = re.compile(
        r'(?P<dest>\d+)\s+(?P<src>\d+)\s+(?P<range>\d+)')
    result_map = []
    for _line in raw_map.splitlines():
        result_map.append({
            'destination': int(p_convert_map.match(_line).group('dest')),
            'source': int(p_convert_map.match(_line).group('src')),
            'range': int(p_convert_map.match(_line).group('range')),
        })
    return result_map


def getDestination(source, translation_map):
    destination = source
    for t_map in translation_map:
        if t_map['source'] <= source <= t_map['source'] + t_map['range']:
            destination = t_map['destination'] + \
                (source - t_map['source'])
            break
    return destination


print('Getting seeds')
seeds = [eval(i) for i in re.findall(
    r'\d+', re.search(r'seeds:\s+(?P<seeds>.*)\s+seed-to-soil map:', data, re.MULTILINE + re.DOTALL).group('seeds'))]
# print(seeds)

print('Getting seed to soil')
seed_to_soil = re.search(r'.*seed-to-soil map:\s+(?P<map_data>.*)\s+soil-',
                         data, re.MULTILINE + re.DOTALL).group('map_data')
seed_to_soil_map = createMap(seed_to_soil)
# print(seed_to_soil_map)

print('Getting soil to fertilizer')
soil_to_fertilizer = re.search(r'.*soil-to-fertilizer map:\s+(?P<map_data>.*)\s+fertilizer-',
                               data, re.MULTILINE + re.DOTALL).group('map_data')
soil_to_fertilizer_map = createMap(soil_to_fertilizer)
# print(soil_to_fertilizer_map)

print('Getting fertilizer to water')
fertilizer_to_water = re.search(r'.*fertilizer-to-water map:\s+(?P<map_data>.*)\s+water-',
                                data, re.MULTILINE + re.DOTALL).group('map_data')
fertilizer_to_water_map = createMap(fertilizer_to_water)
# print(fertilizer_to_water_map)

print('Getting water to light')
water_to_light = re.search(r'.*water-to-light map:\s+(?P<map_data>.*)\s+light-',
                           data, re.MULTILINE + re.DOTALL).group('map_data')
water_to_light_map = createMap(water_to_light)
# print(water_to_light_map)

print('Getting light to temperature')
light_to_temperature = re.search(r'.*light-to-temperature map:\s+(?P<map_data>.*)\s+temperature-',
                                 data, re.MULTILINE + re.DOTALL).group('map_data')
light_to_temperature_map = createMap(light_to_temperature)
# print(light_to_temperature_map)

print('Getting temperature to humidity')
temperature_to_humidity = re.search(r'.*temperature-to-humidity map:\s+(?P<map_data>.*)\s+humidity-',
                                    data, re.MULTILINE + re.DOTALL).group('map_data')
temperature_to_humidity_map = createMap(temperature_to_humidity)
# print(temperature_to_humidity_map)

print('Getting humidity to location')
humidity_to_location = re.search(r'.*humidity-to-location map:\s+(?P<map_data>.*)',
                                 data, re.MULTILINE + re.DOTALL).group('map_data')
humidity_to_location_map = createMap(humidity_to_location)
# print(humidity_to_location_map)

almanac = []

for seed in seeds:
    soil = getDestination(seed, seed_to_soil_map)
    fertilizer = getDestination(soil, soil_to_fertilizer_map)
    water = getDestination(fertilizer, fertilizer_to_water_map)
    light = getDestination(water, water_to_light_map)
    temperature = getDestination(light, light_to_temperature_map)
    humidity = getDestination(temperature, temperature_to_humidity_map)
    location = getDestination(humidity, humidity_to_location_map)

    almanac.append({
        'seed': seed,
        'soil': soil,
        'fertilizer': fertilizer,
        'water': water,
        'light': light,
        'temperature': temperature,
        'humidity': humidity,
        'location': location,
    })

# print(almanac)

print(list(filter(lambda x: x['seed'] == 13, almanac)))

answer = min(almanac, key=lambda x: x['location'])

print(f'Answer: {answer["location"]}')
