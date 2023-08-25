# 342. Power of Four
[Problem Link](https://leetcode.com/problems/power-of-four/)

## Initial Solution
To test if there exists an integer $x$ such that $n = 4^x$, we can rearrange the equation to $x = \log_4n$ and test if $x$ is an integer. 

### Bugs
Since $-2^{31} \leq n \leq 2^{31} - 1$, we have to account for the special case where $n \leq 0$, in which case we can just return `False`.

### Complexity
**Time Complexity:** O(1)

All operations run in constant time.

**Space Complexity:** O(1)

No additional space is used.