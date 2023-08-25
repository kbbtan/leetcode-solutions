# 226. Invert Binary Tree
[Problem Link](https://leetcode.com/problems/invert-binary-tree/)

## Initial Solution

The aim of this problem is to swap the left and right pointers of every node.

Since the order in which we swap these pointers does not matter, we can perform any traversal on the binary tree and swap these pointers along our traversal. At the end, we can return the `root` we are given as inverting the binary tree does not affect the `root`.

### Bugs

As with many tree traversal problems, we need to mind the base case where the tree is empty and account for it.

### Complexity
**Time Complexity:** O(n)

We traverse the tree in linear time.

**Space Complexity:** O(n)

We use O(n) space to maintain a data structure to traverse the tree (queue / stack / etc.).