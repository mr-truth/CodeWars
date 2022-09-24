"""
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet.
ROT13 is an example of the Caesar cipher.
Create a function that takes a string and returns the string ciphered with Rot13.
If there are numbers or special characters included in the string,
they should be returned as they are. Only letters from the latin/english alphabet should be shifted,
like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
"""


def rot13(message):
    rot_13 = ''
    for ch in message:
        byte = ord(ch)
        capital = byte & 32
        byte &= ~capital
        if ord('A') <= byte <= ord('Z'):
            byte -= ord('A')
            byte += 13
            byte %= 26
            byte += ord('A')
        byte |= capital
        rot_13 += chr(byte)
    return rot_13


text = 'Hey You '
print(rot13(text))