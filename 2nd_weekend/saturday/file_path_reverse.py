def reverse_file(read_path, write_path):
    with open(read_path, 'rt') as read_file:
            data = read_file.read()

    with open(write_path, "wt") as write_file:
            write_file.write(data[::-1])

if __name__ == "__main__": #jeżeli jestem uruchamianym plikiem, zrób to:
    reverse_file('plik3.txt', 'plik3_reversed.txt')