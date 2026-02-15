class Solution:
    def firstMissingPositive(self, A: List[int]) -> int:
        for i in range(len(A)):
            if A[i] < 0:
                A[i] = 0
        
        for i in range(len(A)):
            val = abs(A[i])
            if 1 <= val <= len(A):
                if A[val-1] > 0:
                    A[val-1] *= -1
                elif A[val-1] == 0:
                    A[val-1] = -1 * (len(A)+1)
        
        for i in range(1,len(A)+1):
            if A[i-1]>=0:
                return i
        return len(A)+1


# Prerequisites
# Before attempting this problem, you should be comfortable with:
# In-Place Array Modification - Using the input array itself as auxiliary storage to achieve O(1) space
# Cycle Sort - Placing elements at their "correct" indices through swapping
# Index Mapping - Understanding that value v should be at index v-1 for positive integers
# Negative Marking Technique - Using the sign of array elements as boolean flags

# we can do this problem with like hashmaps but the problem is that the time complexity was O(nlogn) we want something that could have performed well like TC be O(n) and space O(n) for that reason we are going to use a different approach 

# we have use that for loop 3 times in one for making negative values postive and then using another for loop for edge cases and using last loop for identifyin the correct answer 

# here is the approach 

# The idea is to use the sign of each element as a flag. If the value at index i is negative, it means i + 1 exists in the array. But there's a catch: the array might already contain negative numbers or zeros, which would interfere with our marking scheme.

# So we first convert all non-positive numbers to 0. Then for each value v in the range [1, n], we mark the element at index v - 1 as negative. If it's already 0, we use a special marker -(n + 1) to indicate presence while keeping it distinguishable.

# Finally, the first non-negative index tells us which number is missing.

# Algorithm
# Replace all negative numbers with 0.
# For each number val (using absolute value to handle already-marked cells):
# If 1 <= val <= n:
# If nums[val - 1] > 0, negate it.
# If nums[val - 1] == 0, set it to -(n + 1).
# Find the first index where nums[i] >= 0 and return i + 1.
# If no such index exists, return n + 1.

