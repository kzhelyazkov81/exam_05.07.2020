import re
n = int(input())
plants = {}
for i in range(n):
    current_plant = {}
    data = input().split('<->')
    plant = data[0]
    rarity = data[1]
    if plant in plants:
        plants[plant]['rarity'] = rarity
    else:
        current_plant['rarity'] = rarity
        current_plant['rating'] = []
        plants[plant] = current_plant

while True:
    command = input()
    if command == 'Exhibition':
        break
    command_expr = r'(\w+): (\w+)(?: - (\d+(?:.\d+)?))?'
    matches = re.finditer(command_expr, command)
    for match in matches:
        action = match.group(1)
        plant = match.group(2)
        if plant not in plants.keys():
            print('error')
            break
        if action == 'Rate':
            rating = int(match.group(3))
            plants[plant]['rating'].append(rating)
        elif action == 'Update':
            new_rarity = match.group(3)
            plants[plant]['rarity'] = new_rarity
        elif action == 'Reset':
            plants[plant]['rating'].clear()
print('Plants for the exhibition:')
for plant in plants:
    if plants[plant]['rating']:
        average_rating = sum(plants[plant]['rating']) / len(plants[plant]['rating'])
    else:
        average_rating = 0
    rarity = plants[plant]['rarity']
    print(f'- {plant}; Rarity: {rarity}; Rating: {average_rating:.2f}')