"""
Passed: 24/08/2023
"""

class Solution:
    def tribonacci(self, n: int) -> int:
        # Base Cases.
        if n == 0:
            return 0

        elif n == 1:
            return 1

        elif n == 2:
            return 1

        else:
            # Keep track of the three previous subsolutions.
            # Python syntax helps to visualize that sub_solutions[-1] refers to the
            # solution for F(i - 1). Similarly, this also applies to F(i - 2) and F(i - 3).
            sub_solutions = [0, 1, 1]

            for i in range(3, n + 1):
                # Calculate new subsolution.
                new_solution = sub_solutions[-1] + sub_solutions[-2] + sub_solutions[-3]

                # Update F(i - 1), F(i - 2) and F(i - 3) for next iteration.
                sub_solutions[-3] = sub_solutions[-2]
                sub_solutions[-2] = sub_solutions[-1]
                sub_solutions[-1] = new_solution

            # The last subsolution calculated will be our desired value.
            return sub_solutions[-1]