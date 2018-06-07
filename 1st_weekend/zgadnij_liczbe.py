import random

def int_input(prompt):
    number = None
    while number is None:
        try:
            number = int(input(prompt))
        except ValueError:
            print('To nie jest liczba.')
    return number

lower = int_input('Podaj dół zakresu: ')
upper = int_input('Podaj górę zakresu: ')
target = random.randint(lower, upper)
guess = None
count = 0

while target != guess:
    count += 1
    guess = int(input('Podaj liczbę: '))
    if guess < target:
        print('Za mało!')
    elif guess > target:
        print('Za dużo')

print('Gratulacje! Ilość ruchów:', count)