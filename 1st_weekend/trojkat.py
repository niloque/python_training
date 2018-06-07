a = 5
b = 2
c = 6

if a > 0 and b > 0 and c > 0:
    if a + b > c and a + c > b and b + c > a:
        print('podane liczby mogą być bokami trójkąta')
    else:
        print('podane liczby nie stworzą trójkąta')
else:
    print('podane liczby nie stworzą trójkąta')


if a < 0 or b < 0 or c < 0:
    print('Nie da się stworzyć trójkąta - któraś długość jest ujemna')
elif a + b > c and a + c > b and b + c > a:
    print('Da się utworzyć trójkąt')
else:
    print('Nie da się stworzyć trójkąta - niespełniona nierówność')