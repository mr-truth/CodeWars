"""
Write a function that takes in a string of one or more words, and returns the same string,
    but with all five or more letter words reversed (Just like the name of this Kata).
Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

"""


def spin_words(sentence):
    lst = list(sentence.split())
    arr = []
    for elem in range(len(lst)):
        if len(lst[elem]) >= 5:
            rev = lst[elem][::-1]
            arr.append(rev)
        else:
            arr.append(lst[elem])
    return " ".join(arr)


string = 'Hi CodeWars'
print(spin_words(string))
