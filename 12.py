"""
Move the first letter of each word to the end of it,
then add "ay" to the end of the word. Leave punctuation marks untouched.

Example:
    pig_it('Pig latin is cool') # igPay atinlay siay oolcay
    pig_it('Hello world !')     # elloHay orldway !
"""


def pig_it(text):
    lst = text.split()
    new_lst = []
    for elem in lst:
        if elem.isalpha():
            new = elem[1:] + elem[0] +"ay"
            new_lst.append(new)
        else:
            new_lst.append(elem)
    return " ".join(new_lst)


string = "Pig latin is cool"
print(pig_it(string))