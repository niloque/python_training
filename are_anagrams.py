def are_anagrams(first, second):
    first_word = {}
    second_word = {}
    for char1 in first.lower():
        first_word[char1] = first_word.get(char1, 0) + 1
    print(first_word)

    for char2 in second.lower():
        second_word[char2] = second_word.get(char2, 0) + 1
    print(second_word)
    if first_word == second_word:
        print('Podane słowa są anagramami')
    else:
        print('Podane słowa (' + first + ' i ' + second + ') nie są anagramami')

are_anagrams('slow', 'wlosy')




