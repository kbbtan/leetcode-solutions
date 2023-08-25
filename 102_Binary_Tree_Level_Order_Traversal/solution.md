# 102. Binary Tree Level Order Traversal
[Problem Link](https://leetcode.com/problems/binary-tree-level-order-traversal)

## Initial Solution

Since we are traversing the tree in level order, we can make use of a breadth-first search (BFS) algorithm using a Queue.

The tricky part is the format which the result needs to be in, namely a list of lists where each list contains the nodes of their corresponding level. We can accomplish this by pushing each node with its level into the queue, i.e. we push `(node, 1)` for nodes on level 1. Then, we can keep track of the level each node belongs to and append them to the correct list in the result.

### Complexity
**Time Complexity:** O(n)
We traverse the binary tree in linear time using BFS.

**Space Complexity:** O(n)
We use linear space to maintain both the result list and the queue.

### Alternatives / Improvements

Instead of using an additional variable to keep track of each node's level, we could use a **separate loop** to operate on each level. We accomplish this by checking the size of the queue after each level is completed, which tells us how many nodes are in the next level to operate on. This would save on a small amount of space, even though the space complexity remains the same.