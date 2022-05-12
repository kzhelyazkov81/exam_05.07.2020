def add(index, string):
    index = int(index)
    if 0 <= index <= len(stops):
        back = stops[:index]
        front = stops[index:]
        new = back + string + front
    else:
        new = stops
    return new


def remove(start, end):
    start = int(start)
    end = int(end)
    if 0 <= start <= end < len(stops):
        back = stops[0:start]
        front = stops[end+1:]
        new = back + front
    else:
        new = stops
    return new


def switch(old_string, new_string):
    if old_string in stops:
        new = stops.replace(old_string, new_string)
    else:
        new = stops
    return new



stops = input()
while True:
    command = input()
    if command == 'Travel':
        break
    command = command.split(':')
    action = command[0]
    if action == 'Add Stop':
        stops = add(command[1], command[2])
    elif action == 'Remove Stop':
        stops = remove(command[1], command[2])
    elif action == 'Switch':
        stops = switch(command[1], command[2])
    print(stops)
print(f'Ready for world tour! Planned stops: {stops}')
