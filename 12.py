"""
Move the first letter of each word to the end of it,
then add "ay" to the end of the word. Leave punctuation marks untouched.

Example:
    pig_it('Pig latin is cool') # igPay atinlay siay oolcay
    pig_it('Hello world !')     # elloHay orldway !
"""


def pig_it(text):
    lst = text.split()
    return lst

string = "Hello world !"
print(pig_it(string))