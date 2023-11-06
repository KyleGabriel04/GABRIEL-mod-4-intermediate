'''Module 3: Individual Programming Assignment 1

Thinking Like a Programmer

This assignment covers your intermediate proficiency with Python.
'''


def shift_letter(letter, shift):

    '''Shift Letter.
    4 points.

    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter.

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    letter =letter.upper()
    shift %= 26

    if ord(letter) + shift <= ord("Z"):
       shift_letter = chr(ord(letter) + shift)

    elif ord(letter) + shift > ord("Z"):
        shift -= ord("Z") - ord(letter) + 1
        shift_letter = chr(ord("A") + shift)

    return shift_letter

letter = str(input("Select a Letter: "))
shift = int(input("Select a Number: "))
shifted_letter = shift_letter(letter,shift)

print(shifted_letter)









def caesar_cipher(message, shift):
    '''Caesar Cipher.s
    6 points.

    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    shift_message = ""
    message = message.upper()
    for char in message:
        if char == " ":
            shift_message += " "
        else:
            shift_character = ord(char) + shift
            if shift_character > ord("Z"):
                shift_character -= 26
            shift_message += chr(shift_character)

    return shift_message


message = input("Type a Message: ")
shift = int(input("Input a Number: "))
shifted_message = caesar_cipher(message, shift)

print(shifted_message)







def shift_by_letter(letter, letter_shift):
    '''Shift By Letter.
    4 points.

    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1,
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    letter = letter.upper()
    shift_value = ord(letter_shift) - ord("A")

    if ord(letter) + shift_value <= ord("Z"):
        shift_letter = chr(ord(letter) + shift_value)
    else:
        shift_value -= ord("Z") - ord(letter) + 1
        shift_letter = chr(ord("A") + shift_value)

    return shift_letter


letter = input("Select a Letter: ")
letter_shift = input("Select a letter to shift by: ")
shifted_letter = shift_by_letter(letter, letter_shift)

print(shifted_letter)


def vigenere_cipher(message, key):
    '''Vigenere Cipher.
    6 points.

    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    message = message.upper()
    key = key.upper()
    shift_message = ""

    for i in range(len(message)):
        if message[i] == " ":
            shift_message += " "
        else:
            shift_value = ord(key[i % len(key)]) - ord("A")
            shift_character = ord(message[i]) + shift_value
            if shift_character > ord("Z"):
                shift_character -= 26
            shift_message += chr(shift_character)

    return shift_message


message = input("Type a Message: ")
key = input("Enter the Key: ")
shifted_message = vigenere_cipher(message, key)

print(shifted_message)