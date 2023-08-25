"""
Passed: 25/08/2023
"""
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        result = []
        curr = root

        while curr != None or len(stack) > 0:
            # Keep traversing down left if it exists.
            while curr != None:
                stack.append(curr)
                curr = curr.left

            # Pop the last element and append it to the result.
            curr = stack.pop()
            result.append(curr.val)

            # Start traversing the right subtree.
            curr = curr.right

        return result