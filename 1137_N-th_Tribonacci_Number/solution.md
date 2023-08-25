# 1137. N-th Tribonacci Number
[Problem Link](https://leetcode.com/problems/n-th-tribonacci-number/)

## Initial Solution
This problem is very similar to [509. Fibonacci Number](../509_Fibonacci_Number/solution.md), using the same logic but expanded to Tribonacci numbers. Refer to that solution for an explanation of the logic used.

### Complexity
**Time Complexity:** O(n)

We iterate on $n$ to calculate the solution for each sub-problem.

**Space Complexity:** O(1)

We only keep track of the solutions for two sub-problems at any given time.