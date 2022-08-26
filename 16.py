"""
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:
    It must start with a hashtag (#).

    All words must have their first letter capitalized.

    If the final result is longer than 140 chars it must return false.

    If the input or the result is an empty string it must return false.

Examples:
    " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
    "    Hello     World   "                  =>  "#HelloWorld"
    ""                                        =>  false
"""


def generate_hashtag(s):
    lst = s.split()
    new = []
    for elem in lst:
        if elem.islower():
            new.append(elem.title())
        else:
            new.append(elem.lower().title())
    tmp = "".join(new)
    if len(tmp) > 140 or len(tmp) == 0:
        return False
    new_str = f"#{tmp}"
    return new_str


string = " Hello there thanks for trying my Kata"
print(generate_hashtag(string))

