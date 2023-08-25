"""
Passed: 25/08/2023
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case where binary tree is empty.
        if root == None:
            return None
        
        else:
            stack = [root]

            while len(stack) > 0:
                curr = stack.pop()
                curr.left, curr.right = curr.right, curr.left

                if curr.left:
                    stack.append(curr.left)

                if curr.right:
                    stack.append(curr.right)

            return root