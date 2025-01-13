message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"

def caesar_decode(message, offset):
    new_message = ''

    for letter in message:
        if letter.isalpha():  # Check if the character is a letter
            if letter.islower():  # Handle lowercase letters
                new_letter = chr((ord(letter) - ord('a') - offset) % 26 + ord('a'))
                new_message += new_letter
            elif letter.isupper():  # Handle uppercase letters
                new_letter = chr((ord(letter) - ord('A') - offset) % 26 + ord('A'))
                new_message += new_letter
        else:
            # Non-alphabet characters remain unchanged
            new_message += letter

    return new_message


new_msg = caesar_decode(message, offset = 10)
print(new_msg)