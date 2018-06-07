x = '*'
N = 4

for i in range(1, N+1):
     print(i*x)

print('')

#To samo:

for i in range(N):
    for j in range(i+1):
        print('*', end='')
    print()