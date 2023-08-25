# 767. Reorganize String
[Problem Link](https://leetcode.com/problems/reorganize-string/)

## Initial Solution

The first idea is to collect a count of all the letters, then keep using different letters until it is not possible.

1. Iterate through `s` and collect a count of each letter in the string. Store these counts in an array `counts` where `counts[i]` references the number of letter `i` (`i = 0` represents `"a"`).

2. Define a `result` string to store the final result.

3. While `result` is not yet the length of `s`: 

    - Iterate through `counts`, using a letter `i` if `counts[i] > 0`, and updating the new `counts[i]`.

    - If there is ever a case where the same letter is used again, it means we have failed and we can return `""`.

4. Return `result` once we have rebuilt the full string.

### Bugs

Consider the test case `s = "abb"`.

Using the algorithm above, because it chooses in order of the alphabet it chooses `a` first, then `b`, then because `b` is the only character left, it fails. However, `bab` should be a valid result.

In order to prevent this, we can choose characters in the order of most common to least common, excluding the last used character. Doing so ensures that we save our least common characters as "separator" characters (i.e. in the above example `a` acts as a "separator" character for the two `b`s.)

## Final Solution
Collect a count of all characters, then keep using the most common character that was not used in the previous position.

1. Iterate through `s` and collect a count of each letter in the string. Store these counts in **a max heap with elements `(count, letter_index)`**.

2. Define a `result` string to store the final result.

3. While `result` is not yet the length of `s`:
    
    - **If the heap is empty, it indicates that there are no valid characters left, so we can return `""`. Otherwise,**

    - **Pop the max item from the heap and use its corresponding character**

    - **Push the last popped element back into the heap, if any**

    - **Keep track of the popped element to push it back in the next iteration, if there are still elements left**

4. Return `result` once we have rebuilt the full string.

### Complexity
**Time Complexity**: O(n)

We iterate through `s` at the start once to get the character counts, and again to rebuild the string. Since the size of the heap is not based on the size of `s`, its push and pop operations happen in constant time relative to the size of the input.

**Space Complexity**: O(n)

We use this space to build the `result` string, which is the same size as `s`.