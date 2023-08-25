"""
Passed: 23/08/2023
"""

class Solution:
    def fib(self, n: int) -> int:
        # Base cases.
        if n == 0:
            return 0

        elif n == 1:
            return 1

        else:
            # Keep track of the two previous subsolutions.
            # Python syntax helps to visualize that sub_solutions[-1] and sub_solutions[-2] refer to the
            # solution for F(i - 1) and F(i - 2) for each iteration.
            sub_solutions = [0, 1]

            for i in range(2, n + 1):
                # Calculate new subsolution.
                new_solution = sub_solutions[-1] + sub_solutions[-2]

                # Update F(i - 1) and F(i - 2) for next iteration.
                sub_solutions[-2] = sub_solutions[-1]
                sub_solutions[-1] = new_solution

            # The last subsolution calculated will be our desired value.
            return sub_solutions[-1]
