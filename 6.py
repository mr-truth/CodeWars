"""
    Your goal in this kata is to implement a difference function,
    which subtracts one list from another and returns the result.
    It should remove all values from list a,
    which are present in list b keeping their order.
        array_diff([1,2],[1]) == [2]
    If a value is present in b, all of its occurrences must be removed from the other:
        array_diff([1,2,2,2,3],[2]) == [1,3]
"""


def array_diff(a, b):
    c = []
    for i in a:
        if (not i in b) and a.count(i) >= 1:
            c.append(i)
    return c


list_a = [1, 2, 2, 2, 3]
list_b = [2]
print(array_diff(list_a, list_b))
