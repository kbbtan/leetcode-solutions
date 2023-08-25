# 97. Interleaving String
[Problem Link](https://leetcode.com/problems/interleaving-string/)

## Initial Solution
This question appears to be suited for a Dynamic Programming approach. 

At each `s3` up to length `k`, there is the option of taking the character from either `s1` or `s2`. We also need to keep track of lengths `i` and `j` from `s1` and `s2` respectively such that we know which characters we are considering for `s3`. 

Hence, we can define our sub-problem in terms of `i`, `j` and `k`. Since `k = i + j`, we can apply Dynamic Programming on just `i` and `j`.

We build the following memoization table `memo`, where `x = s1.length` and `y = s2.length`:

| i/j | 0 | 1 | ... | y  |
| ---  | ---  | ---  | ---  | --- |
| 0 | True | | | |
| 1 | | | | |
| ... | | | | |
|x | | | | |

Note that while `i` and `j` refer to the indicies of the table, they refer to the **lengths** of substrings from `s1` and `s2` respectively. This allows us to reserve `memo[0][0]` for the base case where we consider the empty strings `s1 = ""` and `s2 = ""`. We define this case to be `True` as `s3 = ""` is a valid solution for this case.

Then, each subsequent entry `memo[i][j]` represents whether substring `s3` of length `k` can be formed by interleaving substring `s1` of length `i` and substring `s2` of length `j`.

For cases where `i == 0`, we check if `memo[0][j-1]` is `True`, and if so, `memo[0][j]` is `True` if we can add character `s2[j-1]`. Similarly, we apply the same reasoning to cases where `j == 0`.

Otherwise, we need to check for both cases following the reasoning above. Namely, we need to check if: 
- We can add `s2[j-1]` if `memo[i][j-1]` is `True`
- We can add `s1[i-1]` if `memo[i-1][j]` is `True`.

If **either** of these cases pass, we define `memo[i][j]` to be `True`.

After constructing `memo`, `memo[x][y]` will give us the answer when we consider the entire strings.

### Bugs

This algorithm assumes that `s1.length + s2.length == s3.length`, and will run into errors when this condition is not met. Since we know it is impossible to interleave `s3` in this case, we can check for it at the start and return `False` immediately.

## Final Solution

Apply the Dynamic Programming algorithm as described above, but with the additional base case considered where the lengths of the strings are not suitable.

### Complexity
**Time Complexity:** O(xy)

We build the `memo` table in O(xy) time.

**Space Complexity:** O(xy)

The `memo` table takes up O(xy) space.

### Alternatives / Improvements

#### BFS / DFS

We can also construct a graph using the two strings `s1` and `s2`, then traverse it to attempt to find a valid solution, as described [here](https://leetcode.com/problems/interleaving-string/solutions/31948/8ms-c-solution-using-bfs-with-explanation/). While it has the same time and space complexity, some might find this solution more intuitive to understand.