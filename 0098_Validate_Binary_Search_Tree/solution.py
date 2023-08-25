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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        last_entry = None

        # In-order traversal implentation using stack.
        stack = []
        curr = root

        while curr != None or len(stack) > 0:
            # Keep traversing down left until not possible.
            while curr != None:
                stack.append(curr)
                curr = curr.left

            # Pop from stack and set to right.
            curr = stack.pop()
            
            # Check if values are still in order.
            if last_entry == None:
                last_entry = curr.val

            else:
                # Note that BST keys are unique by definition.
                if curr.val <= last_entry:
                    return False

                else:
                    last_entry = curr.val

            curr = curr.right

        # Whole tree traversed without issues.
        return True