# Napisać program sprawdzający czy dana liczba całkowita jest kwadratem innej liczby

x = 144
y = (int(x ** 0.5))

if y ** 2 == x:
    print('Dana liczba jest kwadratem liczby:', y)
else:
    print('Dana liczba nie jest kwadratem innej liczby')


z = 101

for i in range(0, z+1):
    if i ** 2 == z:
        print('z to kwadrat liczby', i)
        break
else:
    print('z nie jest kwadratem')