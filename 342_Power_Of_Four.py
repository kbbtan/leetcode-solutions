"""
Simple solution using Math.

Problem Link: https://leetcode.com/problems/power-of-four/
Last Updated: 22/08/2022
"""

import math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        
        else:
            return math.log(n, 4).is_integer()

if __name__ == "__main__":
    s = Solution()

    # Provided Examples.
    assert s.isPowerOfFour(16) == True
    assert s.isPowerOfFour(5) == False
    assert s.isPowerOfFour(1) == True

    # Also test for negative inputs.
    assert s.isPowerOfFour(-412) == False

    print("All Tests Passed")