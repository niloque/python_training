def frequency(text):
    histogram = {}
    for char in text.lower():
        if char.isalpha():
            histogram[char] = histogram.get(char, 0) + 1
        else:
            histogram['others'] = histogram.get('others', 0) + 1
    return histogram


print(frequency('Abraham123'))

