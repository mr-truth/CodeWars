"""
Given an n x n array, return the array elements arranged
from outermost elements to the middle element, traveling clockwise.

    array = [[1,2,3],
             [4,5,6],
             [7,8,9]]
    snail(array) #=> [1,2,3,6,9,8,7,4,5]

For better understanding,
please follow the numbers of the next array consecutively:

    array = [[1,2,3],
            [8,9,4],
            [7,6,5]]
    snail(array) #=> [1,2,3,4,5,6,7,8,9]
NOTE: The idea is not sort the elements from the lowest value to the highest;
the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as
en empty array inside an array [[]].
"""


def snail(snail_map):
    new = []
    row_start = 0
    row_end = len(snail_map) - 1
    col_start = 0
    col_end = len(snail_map[0]) - 1

    while row_start <= row_end and col_start <= col_end:
        for i in range(col_start, col_end+1):
            new.append(snail_map[row_start][i])
        row_start += 1

        for i in range(row_start, row_end+1):
            new.append(snail_map[i][col_end])
        col_end -= 1

        if row_start <= row_end:
            for i in range(col_end, col_start - 1, -1):
                new.append(snail_map[row_end][i])
        row_end -= 1

        if col_start <= col_end:
            for i in range(row_end, row_start - 1, -1):
                new.append(snail_map[i][col_start])
        col_start += 1

    return new


array = [[1, 2, 3],
         [8, 9, 4],
         [7, 6, 5]]
print(snail(array))
