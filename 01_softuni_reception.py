efficiency = []
for i in range(3):
    efficiency.append(int(input()))
number_of_students = int(input())
hours = 0
hours_for_brake = 0
while number_of_students > 0:
    hours += 1
    for i in efficiency:
        number_of_students -= i
    if hours % 3 == 0 and number_of_students > 0:
        hours_for_brake += 1

total_time = hours + hours_for_brake
print(f'Time needed: {total_time}h.')
