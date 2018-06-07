from homework.peseltools import *

pesel = int_input("Podaj PESEL: ")

display = extract_personal_data(pesel)

print("Date of birth:", display["birth_date"])
print("Sex:", display["sex"])