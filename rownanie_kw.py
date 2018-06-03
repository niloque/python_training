a = 1
b = 5
c = 6

delta = b ** 2 - (4 * a * c)

if delta == 0:
    print('Rozwiązanie: x0 =', -b / (2 * a))
elif delta > 0:
    x1 = (-b - delta ** 0.5) / (2 * a)
    x2 = (-b + delta ** 0.5) / (2 * a)
    print('Rozwiązania:')
    print('x1 =', x1)
    print('x2 =', x2)
else:
    print('Brak rozwiązań')


