"""
To find the number of ways a traveller can travel in a m x n grid.
He has to travel from the top left corner (start) of the grid to the bottom right corner (end).
Conditions:
He can move only one step at a time and that too, either right or down
"""
"""
Solution:
base case: a grid of 1 x 1, he is already there in the end point. So just one way to get from start to end
another base case: return 0 if m or n is zero

recursively trying to get all the possible ways for RIGHT and DOWN moves
if he takes right, it means he is reducing one column
if he takes down, it means he is reducing one row
"""


def grid_traveller(m, n):
    # base case 1
    if m == 1 and n == 1:
        return 1
    # base case 2
    if m == 0 or n == 0:
        return 0

    return grid_traveller(m - 1, n) + grid_traveller(m, n - 1)


print(grid_traveller(10, 10))
