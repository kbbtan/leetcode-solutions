# 98. Validate Binary Search Tree
[Problem Link](https://leetcode.com/problems/validate-binary-search-tree/)

## Initial Solution

We can perform an [in-order traversal](../94_Binary_Tree_Inorder_Traversal/solution.md) of the binary tree. If the traversal is strictly increasing, it is a valid binary search tree. Since the question specifies that the number of nodes is in the range $[1, 10^4]$, we can avoid testing for the edge case where `root == None`.

### Complexity
**Time Complexity:** O(n)
We traverse the BST in linear time.

**Space Complexity:** O(n)
We maintain a stack of the nodes in order to perform in-order traversal.