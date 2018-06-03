lista = [4, 8, 1, 3, 5]

for idx, value in enumerate(lista):
    if idx == 0:
        current_min = value
        current_max = value
    elif current_max < value:
        current_max = value
    elif current_min > value:
        current_min = value

print('Maksimum:', current_max)
print('Minimum:', current_min)