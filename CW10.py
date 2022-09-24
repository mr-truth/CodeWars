"""
You are given an array (which will have a length of at least 3, but could be very large) containing integers.
The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N.
Write a method that takes the array as an argument and returns this "outlier" N.

Examples:
    [2, 4, 0, 100, 4, 11, 2602, 36]
    Should return: 11 (the only odd number)

    [160, 3, 1719, 19, 11, 13, -21]
    Should return: 160 (the only even number)
"""


def find_outlier(integers):
    tmp_lst1 = []
    tmp_lst2 = []
    for elem in range(len(integers)):
        if integers[elem] % 2 == 0:
            tmp_lst1.append(integers[elem])
        elif integers[elem] % 2 != 0:
            tmp_lst2.append(integers[elem])
    if len(tmp_lst2) > len(tmp_lst1):
        return tmp_lst1[0]
    else:
        return tmp_lst2[0]


lst = [2, 4, 0, 100, 4, 11, 2602, 36]
print(find_outlier(lst))
