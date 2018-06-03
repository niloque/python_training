total = 0.0
count = 0
number = 0

while number >= 0:
    number = float(input('Podaj liczbę: '))
    if number >= 0:
        total += number
        count += 1

if count == 0:
    print('Nie podano ani jednej nieujemnej liczby')
else:
    print('Podano tyle nieujemnych liczb: ', count)
    print('Ich średnia: ', total / count)