list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
output = []

for i in range(len(list1)):
    output.append(list1[i])
    output.append(list2[i])

print(output)

output2 = []
for i, value in enumerate(list1):
    output2.append(value)
    output2.append(list2[i])
print(output2)

output3 = []
for first, second in zip(list1, list2):
    output3.append(first)
    output3.append(second)

print(output3)