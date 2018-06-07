# Napisać program obliczający sumę liczb parzystych niewiększych niż 100

total = 0

for i in range (2, 101, 2):
#   total = total + i
    total += i

print('Suma: ', total)

# albo prościej:

print('Suma: ', sum(range(2, 101, 2)))