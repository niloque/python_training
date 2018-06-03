mapping = {'bar': 'foo', 'spam': 'eggs', 'baz': 'foo'}

# {'foo': ['bar', 'baz'], 'eggs': ['spam']}

reversed = {}

for key, value in mapping.items():
    if value not in reversed:
        reversed[value] = [key]
    else:
        reversed[value].append(key)

print(reversed)