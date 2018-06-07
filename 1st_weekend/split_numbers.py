numbers = '123,21,37,3'

"""
def split(text, sep):
    parts = []
    current_part = ''
    for char in text:
        if char != sep:
            current_part += char
        else:
            parts.append((current_part))
            current_part = ''
    parts.append(current_part)
    return parts
"""

print('')

#alternative:

def split(text, sep):
    parts = []
    current_part = []
    for char in text:
        if char != sep:
            current_part.append(char)
        else:
            parts.append(''.join(current_part))
            current_part = []
    parts.append(''.join(current_part))
    return parts


def split3(text, sep):
    parts = []
    start = 0
    for current, char in enumerate(text):
        if char == sep:
            parts.append(text[start:current])
            start = current + 1
    parts.append(text[start:])
    return parts

print(split3(numbers, ','))
print(split3(numbers, ',') == ['123', '21', '37', '3'])