# 94. Binary Tree Inorder Traversal
[Problem Link](https://leetcode.com/problems/binary-tree-inorder-traversal/)

## Initial Solution

This question requires us to implement a [binary tree inorder traversal](https://www.freecodecamp.org/news/binary-search-tree-traversal-inorder-preorder-post-order-for-bst/). 

In summary, we aim to output the nodes in order of:
1. All nodes in left subtree
2. Parent node
3. All nodes in right subtree

for all subtrees that exist in the binary tree.

This can be done through the following principles:
1. Use a `curr` pointer to traverse down `left` while pushing these nodes into a `stack`
2. Once the end is reached (no left subtree remains), pop the last node and output its value
3. Set `curr` to the `right` of this node and repeat from step 1

continue this process until both the `stack` and `curr` are empty.


### Complexity
**Time Complexity:** O(n)

We traverse the nodes in the binary tree in linear time.

**Space Complexity:** O(n)

We use additional O(n) space to maintain the stack and result array.