import re

# input_file = 'example_part1.txt'
input_file = 'puzzle_input.txt'

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


def getSource(destination, translation_map):
    source = destination
    for t_map in translation_map:
        if t_map['destination'] <= destination <= t_map['destination'] + t_map['range']:
            source = t_map['source'] + \
                (destination - t_map['destination'])
            break
    return source


def getSeedRanges(sources):
    seed_ranges = []
    sets = re.findall(r'\d+ \d+', sources)
    # print(sets)
    for set in sets:
        seed_ranges.append({
            'start': int(set.split(' ')[0]),
            'range': int(set.split(' ')[1]),
        })
    return seed_ranges


print('Getting seed sources')
seed_sources = re.search(r'seeds:\s+(?P<seeds>.*)\s+seed-to-soil map:',
                         data, re.MULTILINE + re.DOTALL).group('seeds')
# print(seed_sources)

print('Getting seed ranges')
seed_ranges = getSeedRanges(seed_sources)
# print(seed_ranges)

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

# print('Getting light to temperature')
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


# Work back from lowest possible locations to seed
# [{'destination': 60, 'source': 56, 'range': 37}, {'destination': 56, 'source': 93, 'range': 4}]
lowest_location_map_range = min(
    humidity_to_location_map, key=lambda x: x['destination'])

lowest_location_range = {
    'destination': 0,
    'source': 0,
    'range': lowest_location_map_range['source'] + lowest_location_map_range['range']
}

print('Getting lowest location (reverse lookup)')
lowest_location = -1
print(f'Location range: {lowest_location_range}')

for location in range(lowest_location_range['destination'], lowest_location_range['destination'] + lowest_location_range['range']):
    humidity = getSource(location, humidity_to_location_map)
    temperature = getSource(humidity, temperature_to_humidity_map)
    light = getSource(temperature, light_to_temperature_map)
    water = getSource(light, water_to_light_map)
    fertilizer = getSource(water, fertilizer_to_water_map)
    soil = getSource(fertilizer, soil_to_fertilizer_map)
    seed = getSource(soil, seed_to_soil_map)

    # Check if the seed is in any of the ranges
    for s_range in seed_ranges:
        if seed in range(s_range['start'], s_range['start'] + s_range['range']):
            lowest_location = location
            print(f'Lowest location found! -> {location}')
            break

    if lowest_location != -1:
        break

answer = lowest_location

print(f'Answer: {answer}')
