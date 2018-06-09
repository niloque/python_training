def lines_histogram2(input_file):
    result = {}
    for line in input_file:
        key = len(line.rstrip('\r\n'))
        result[key] = result.get(key, 0) + 1
    return result

if __name__ == "__main__":
    try:
        with open(path, "rt") as in_file:
            print(lines_histogram2(in_file))
    except OSError as err:
        print(err)


lines_histogram2()