def is_palindrome(text):
    """
    Checks if text is palindrome

    Args:
        text: string to be checked
    Returns:
        True if text is palindrome, False otherwise
    """
    text = text.lower()
    for i in range(len(text) // 2):
        if text[i] != text[len(text)-i-1]:
            return False
    return True

print(is_palindrome('Oko'))




print(len('Kornel'))


text2 = 'Kornel'
for i in range(len(text2)):
    print(text2[i], end='')