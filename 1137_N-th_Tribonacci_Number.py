"""
Basic Dynamic Programming Template.
Notice that we only really need to store solutions for n, n-1 and n-2 at a time.

Problem Link: https://leetcode.com/problems/n-th-tribonacci-number/
Last Updated: 22/08/2022
"""

class Solution:
    def tribonacci(self, n: int) -> int:
        memo = [0, 1, 1]

        if n < 3:
            return memo[n]

        else:
            curr_n = 2

            while curr_n < n:
                new_tribonacci = sum(memo)
                memo = [memo[1], memo[2], new_tribonacci]
                curr_n += 1

            return memo[-1]

if __name__ == "__main__":
    s = Solution()

    # Provided Examples.
    assert s.tribonacci(4) == 4
    assert s.tribonacci(25) == 1389537

    # Test the Maximum Bound. 
    assert s.tribonacci(37) == 2082876103

    print("All Tests Passed")