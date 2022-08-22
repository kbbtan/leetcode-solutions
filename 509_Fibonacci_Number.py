"""
Basic Dynamic Programming Template.

Problem Link: https://leetcode.com/problems/fibonacci-number/
Last Updated: 22/08/2022
"""

class Solution:
    def fib(self, n: int) -> int:
        memo = {}

        def helper(n):
            if n <= 1:
                return n

            else:
                if n-1 in memo:
                    one_lower = memo[n-1]

                else:
                    one_lower = helper(n - 1)
                    memo[n-1] = one_lower

                if n-2 in memo:
                    two_lower = memo[n-2]

                else:
                    two_lower = helper(n - 2)
                    memo[n-2] = two_lower

                return one_lower + two_lower

        return helper(n)

if __name__ == "__main__":
    s = Solution()

    # Provided Examples.
    assert s.fib(2) == 1
    assert s.fib(3) == 2
    assert s.fib(4) == 3

    # Test the Maximum Bound.
    assert s.fib(30) == 832040

    print("All Tests Passed")