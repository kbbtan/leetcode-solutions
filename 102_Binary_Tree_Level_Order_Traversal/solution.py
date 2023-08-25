"""
Passed: 25/08/2023
"""
from typing import Optional, List
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Base case where tree is empty.
        if root == None:
            return []

        else:
            result = []
            queue = collections.deque([(root, 0)])

            # Keep track of what level we're currently on.
            level_result = []
            level = 0

            # Perform BFS.
            while len(queue) > 0:
                curr, curr_level = queue.popleft()

                # Update the result.
                if curr_level > level:
                    # We have moved to the next level.
                    # Append the last level to result and update our tracker.
                    result.append(level_result)
                    level_result = [curr.val]
                    level += 1

                else:
                    # Keep adding to the same level.
                    level_result.append(curr.val)

                # Add children to the queue.
                if curr.left:
                    queue.append((curr.left, curr_level + 1))

                if curr.right:
                    queue.append((curr.right, curr_level + 1))

            # Add the last level to result.
            result.append(level_result)

            return result