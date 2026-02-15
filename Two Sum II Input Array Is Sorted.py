class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l , r, = 0, len(numbers)-1
        while l<r:
            curSum = numbers[l] + numbers[r]
            if curSum>target:
                r-=1
            elif curSum<target:
                l+=1
            else:
                return[l+1,r+1]


# Time & Space Complexity
# Time complexity: O(n)
# Space complexity: O(1)


# Before attempting this problem, you should be comfortable with:

# Two Pointers technique - Using pointers at both ends of a sorted array and moving them based on sum comparison
# Binary Search - Efficiently finding a target value in a sorted array in O(log n) time
# Hash Maps - Storing values and indices for O(1) lookup of complements

# Common Pitfalls
# Returning 0-Indexed Instead of 1-Indexed Results
# The problem explicitly requires 1-indexed positions in the output. A common mistake is returning [i, j] instead of [i + 1, j + 1]. Always double-check the problem requirements for indexing conventions, as returning 0-indexed results will be marked as incorrect.

# Not Leveraging the Sorted Property
# Since the array is already sorted, the two-pointer approach achieves O(n) time with O(1) space. Using a hash map still works but wastes the sorted property and uses O(n) extra space unnecessarily. While not incorrect, failing to recognize and use the sorted property results in a suboptimal solution
