"""
Solved using a Greedy approach.

Initially tried going from s to the target.
Figured out going from the target to s is better.
This ensures that intermediate steps work toward a valid solution.

Problem Link: https://leetcode.com/problems/stamping-the-sequence/
Last Updated: 22/08/2022
"""

from typing import List

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        possible_stamps = []

        for i in range(len(stamp)):
            for j in range(len(stamp) - i):
                possible_stamps.append("?" * i + stamp[i:len(stamp)-j] + "?" * j)
        
        moves = []
        num_attempt = 0

        while target != "?" * len(target):
            found = False

            for i in range(len(target) - len(stamp) + 1):
                if target[i:i+len(stamp)] in possible_stamps:
                    target = target[:i] + "?" * len(stamp) + target[i+len(stamp):]
                    moves.append(i)
                    found = True
                    break

            num_attempt += 1

            if not found:
                return []

            if num_attempt == 10 * len(target):
                return []

        return moves[::-1]

if __name__ == "__main__":
    s = Solution()

    # Provided Examples.
    assert s.movesToStamp("abc", "ababc") == [0, 2]
    assert s.movesToStamp("abca", "aabcaca") == [3, 0, 1]

    print("All Tests Passed")