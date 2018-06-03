x = int(input('podaj x: '))

if x < 0 and x % 2 == 0:
    print('x ujemny parzysty')
elif x < 0:
    print('x ujemny nieparzysty')
elif x == 0:
    print('x równy 0')
elif x == 10:
    print('x równy 10')
else:
    print('x dodatni, różny od 10')