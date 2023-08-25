"""
Passed: 25/08/2023
"""

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Base case where the lengths are not suitable.
        if len(s1) + len(s2) != len(s3):
            return False

        else:
            x = len(s1)
            y = len(s2)

            memo = [[None for j in range(y + 1)] for i in range(x + 1)]

            # Base case for i = 0 and j = 0.
            memo[0][0] = True

            # Base cases for i = 0 or j = 0.
            for i in range(1, x + 1):
                memo[i][0] = memo[i-1][0] and s1[i-1] == s3[i-1]

            for j in range(1, y + 1):
                memo[0][j] = memo[0][j-1] and s2[j-1] == s3[j-1]

            # General cases.
            for i in range(1, x + 1):
                for j in range(1, y + 1):
                    memo[i][j] = (memo[i-1][j] and s1[i-1] == s3[i+j-1]) or (memo[i][j-1] and s2[j-1] == s3[i+j-1])
            
            return memo[x][y]