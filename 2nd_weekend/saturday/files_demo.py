my_file = None
try:
    my_file = open('plik.txt', 'rt')
    data = my_file.read()
    print(data)
except OSError as err:
    print("Error:",str(err))
finally:
    if my_file is not None:
        print("Zamykam")
        my_file.close()
print()
print("-----")
print()

#zalecana konstrukcja do otwierania pliku:

try:
    with open('plik2.txt') as my_file: #w open pominięte argumenty, 'rt' = default
        print(my_file.read())
except OSError as err:
    print(err)


with open('plik3.txt', 'wt') as out_file: # zapisywanie pliku (jeśli już istnieje, to zostaje nadpisany)
    out_file.write('inny tekst niz oryginalny')

with open("plik.txt") as my_file:
    lines = my_file.readlines()
    print(lines)
    for i in lines:
        print(lines[i])
        lines[i].rstrip("\n")

with open("plik.txt") as my_file:
    for line in my_file:
        print(line)

text = "some text"
print(text.rstrip("t"))