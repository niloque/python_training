"""
def int_input(prompt):
    number = None
    while number is None:
        try:
            number = int(input(prompt))
        except ValueError:
            print('To nie jest liczba całkowita')

silnia = int_input('Podaj liczbę całkowitą: ')
"""

def factorial(n):
    if n < 0:
        raise ValueError('Factorial is defined only for nonnegative integers')
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(factorial(0))
