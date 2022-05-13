"""
To find the number of ways a traveller can travel in a m x n grid.
He has to travel from the top left corner (start) of the grid to the bottom right corner (end).
Conditions:
He can move only one step at a time and that too, either right or down
"""
"""
Recursive Solution:
base case: a grid of 1 x 1, he is already there in the end point. So just one way to get from start to end
another base case: return 0 if m or n is zero

recursively trying to get all the possible ways for RIGHT and DOWN moves
if he takes right, it means he is reducing one column
if he takes down, it means he is reducing one row

Levels : m + n
Time Complexity: O(2 ^ (m+n))
Space Complexity: O(m+n)

Memoization Solution:
If observed that grid_traveller(a,b) = grid_traveller(b,a)
Just the grid is flipped, but number of ways remain the same

Possible values of child nodes:
m = {0,1,2,3,4,..m-1) -> m number of nodes
n = {0,1,2,3,..n-1) -> n number of nodes

Number of nodes : m * n

Time Complexity: O(m*n)
Space Complexity: O(m+n)

"""


def grid_traveller(m, n, memo={}):
    key = str(m) + "," + str(n)
    # check if args in memo
    if key in memo:
        return memo[key]
    # base case 1
    if m == 1 and n == 1:
        return 1
    # base case 2
    if m == 0 or n == 0:
        return 0

    memo[key] = grid_traveller(m - 1, n, memo) + grid_traveller(m, n - 1, memo)
    return memo[key]


print(grid_traveller(2, 3))
print(grid_traveller(10, 10))
print(grid_traveller(20, 20))
