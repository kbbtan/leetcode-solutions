# 509. Fibonacci Number
[Problem Link](https://leetcode.com/problems/fibonacci-number/)

## Initial Solution
This is an introductory dynamic programming problem where the solution relies on the solutions of several sub-problems. In this example, the solution for $F(n)$ relies on the solutions of $F(n-1)$ and $F(n-2)$, making it ideal for a dynamic programming solution.

The base cases for this algorithm is as defined in the problem, $F(0) = 0$ and $F(1) = 1$. In these cases, we can simply output the corresponding solution.

For the inductive cases $n \geq 2$, we can solve F(n) iteratively up until $n - 1$, and then use $F(n-1)$ and $F(n-2)$ to solve $F(n)$. Since each solution only relies on two previous sub-problems, we only need two variables to store these solutions at any time.

### Complexity
**Time Complexity:** O(n)
We iterate on $n$ to calculate the solution for each new sub-problem.

**Space Complexity:** O(1)
We only keep track of the solutions for two sub-problems at any given time.