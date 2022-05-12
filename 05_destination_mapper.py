import re
places = input()
travel_points = 0
destinations = []
regex = r'(=|\/)([A-Z][A-Za-z]{2,})\1'
matches = re.finditer(regex, places)

for match in matches:
    destinations.append(match.group(2))

for destination in destinations:
    travel_points += len(destination)

destinations = ', '.join(destinations)

print(f'Destinations: {destinations}')
print(f'Travel Points: {travel_points}')