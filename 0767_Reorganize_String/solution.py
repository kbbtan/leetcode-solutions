"""
Passed: 23/08/2023
"""
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = [0 for _ in range(26)]
        count_heap = []
        last_heap_element = None
        result = ""

        # Collect count of each letter.
        for c in s:
            counts[ord(c) - 97] += 1

        # Move the counts to a heap.
        # Add the negative counts to simulate a max heap (Python assumes a min heap).
        for i, count in enumerate(counts):
            if count > 0:
                heapq.heappush(count_heap, (-count, i))

        # Attempt to rebuild the string by character.
        while len(result) < len(s):
            # There are no more valid characters to use. Failed case.
            if len(count_heap) == 0:
                return ""

            # Update the result with the most common character which was not last used.
            most_common = heapq.heappop(count_heap)
            result += chr(most_common[1] + 97)

            # Add back the last heap element used, if any.
            if last_heap_element:
                heapq.heappush(count_heap, last_heap_element)
                last_heap_element = None

            # If there are still elements left, we add the element back on the next iteration.
            # This is because it is "illegal" to use it again in the next immediate round.
            # Otherwise we can just discard it.
            if most_common[0] < -1:
                last_heap_element = (most_common[0] + 1, most_common[1])


        # We have rebuilt the string if this point is reached.
        return result