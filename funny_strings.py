import random

def bubbleize(text):
    string = ''
    for i in range(len(text)):
        if i % 2 != 0:
            string += text[i].upper()
        else:
            string += text[i].lower()
    return string


def randomize(text):
    string = ''
    for char in text:
        rand = random.randint(1, 10)
        if rand % 2 != 0:
            string += char.upper()
        else:
            string += char.lower()
    return string


def numberize(text):
    string = ''
    for char in text:
        if char == 'o':
            string += '0'
        elif char == 'e':
            string += '3'
        elif char == 'i':
            string += '!'
        elif char == 'a':
            string += '@'
        elif char == 'A':
            string += '4'
        else:
            string += char
    return string