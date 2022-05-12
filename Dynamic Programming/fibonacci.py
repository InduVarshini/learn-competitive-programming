"""
Using memoization to optimize the O(2^N) time complexity of the original recursive solution
to the fibonacci problem

Memoization: Storing the answers of sub-problems
Using a hashmap datastructure for quick access : Here -- dict
n: as keys
fib(n) : as values of the dict

Result: Time Complexity : O(n), Space Complexity : O(n)
"""


def fib(n, memo={}):
    # new base case to check if the value is already present in the memo
    if n in memo: return memo[n]

    # actual base case
    if n <= 2: return 1

    # if value not found in the memo, calculate and add it in the memo
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


print(fib(50))
