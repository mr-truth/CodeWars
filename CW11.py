"""
Write an algorithm that takes an array and moves all of the zeros to the end,
preserving the order of the other elements.

Example:
    move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""


def move_zeros(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-i-1):
            if lst[j] == 0:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


arr = [1, 0, 1, 2, 0, 1, 3]
print(move_zeros(arr))
