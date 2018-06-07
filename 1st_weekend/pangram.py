import string

def is_pangram(text):
    text = text.lower()
    for letter in string.ascii_lowercase:
        if letter not in text:
            return False
    return True

pang = "Pack my box with five dozen liquor jugs."
not_pang = "Mam na imię Kornel"



def is_pangram2(text):
    found_letters = {}
    for char in text.lower():
        if char.isalpha():
            found_letters[char] = 0
    if len(found_letters) == len(string.ascii_lowercase):
        return True
    return False

print(is_pangram2(pang))
print(is_pangram2(not_pang))