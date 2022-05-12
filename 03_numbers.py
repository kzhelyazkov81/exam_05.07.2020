numbers = list(map(int, input().split(' ')))

average_value = sum(numbers) / len(numbers)

top_numbers = []
while len(top_numbers) < 5:
    max_number = max(numbers)
    if max_number <= average_value:
        break
    if max_number > average_value:
        top_numbers.append(max_number)
        numbers.remove(max_number)

if len(top_numbers) == 0:
    print('No')
else:
    top_numbers = list(map(str, top_numbers))
    top_numbers = ' '.join(top_numbers)
    print(top_numbers)
