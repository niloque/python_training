def lines_histogram(input_path):
    result = {}
    with open(input_path, "rt") as in_file:
        for line in in_file:
            stripped = line.rstrip('\r\n')
            result[len(stripped)] = result.get(stripped, 0) + 1
    return result

if __name__ == "__main__":
    path = input("Podaj ścieżkę: ")
    try:
        print(lines_histogram())
    except OSError as err:
        print(err)


"""
with open("plik.txt") as my_file:
    lines = my_file.readlines()
    lines2 = ([i.rstrip("\n") for i in lines])

    for word in lines2:
        histogram[len(word)] = histogram.get(len(word), 0) + 1

print(lines2)
print(histogram)
"""

