def swap(values, index1, index2):
    index1 = int(index1)
    index2 = int(index2)
    values[index1], values[index2] = values[index2], values[index1]
    return values


def multiply(values, index1, index2):
    index1 = int(index1)
    index2 = int(index2)
    element = values[index1] * values[index2]
    values[index1] = element
    return values


def decrease(values):
    for i in range(len(values)):
        values[i] -= 1
    return values


array = list(map(int, input().split(' ')))

while True:
    command = input()
    if command == 'end':
        break
    else:
        command = command.split(' ')
    if command[0] == 'swap':
        array = swap(array, command[1], command[2])
    elif command[0] == 'multiply':
        array = multiply(array, command[1], command[2])
    elif command[0] == 'decrease':
        array = decrease(array)

array = list(map(str, array))
array = ', '.join(array)
print(array)
