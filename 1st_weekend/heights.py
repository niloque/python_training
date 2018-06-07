data = [{'first_name': 'John', 'last_name': 'Doe', 'height': 173},
        {'first_name': 'James', 'last_name': 'Kovalsky', 'height': 183},
        {'first_name': 'John', 'last_name': 'Smith', 'height': 165},
        {'first_name': 'Ann', 'last_name': 'Novak', 'height': 170}]

# średnia wzrostu wszystkich

total = 0
for record in data:
#    print(record['height'])
    total += record['height']

print('Średnia:', total / len(data))

# średnia wzrostów ludzi posiadająych to samo imię.

heights_by_name = {}

for record in data:
    if record['first_name'] in heights_by_name:
        heights_by_name[record['first_name']].append(record['height'])
    else:
        heights_by_name[record['first_name']] = [record['height']]

print(heights_by_name)

print('')
for name, heights in heights_by_name.items():
    print(name, sum(heights) / len(heights))

print('')

#alternatywny sposób:

total_by_name = {}
count_by_name = {}

for record in data:
    first_name = record['first_name']
    if first_name in total_by_name:
        total_by_name[first_name] += record['height']
        count_by_name[first_name] += 1
    else:
        total_by_name[first_name] = record['height']
        count_by_name[first_name] = 1

for name, total in total_by_name.items():
    print(name, total / count_by_name[name])

print('')
# z getem:

for record in data:
    first_name = record['first_name']
    total_by_name[first_name] = total_by_name.get(first_name, 0) + record['height']
    count_by_name[first_name] = count_by_name.get(first_name, 0) +1

for name, total in total_by_name.items():
    print(name, total / count_by_name[name])