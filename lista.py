numbers = [1, 4, -3, 0]
empty = []

print('Element o indeksie 1:', numbers[1])
print('Liczba elementów na liście:',len(numbers))
numbers[2] = 10
print('Element o indeksie 1 to:', numbers[2])

elementy = len(numbers)

for i in range(elementy):
    print(numbers[i])

print(' ')

#for value in numbers:
#    print(value)

print(' ')

for i in range(elementy-1, -1, -1):
    print(numbers[i])

print(' ')

for value in reversed(numbers):
    print(value)

print(' ')

for a, b in enumerate(numbers):
    print(a, b)

for pair in enumerate(numbers):
    print(pair)

numbers.append(100)
numbers.append(200)

print(numbers)
del numbers[5]
print(numbers)
numbers.remove(100)
print(numbers)