x = 1
y = 3
z = 1

if x <= y <= z or z <= y <= x:
    print('mediana to y =', y)
elif y <= x <= z or z <= x <= y:
    print('mediana to x =', x)
else:
    print('mediana to z =', z)
