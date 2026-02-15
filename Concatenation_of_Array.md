1. Iteration (Two Pass)
Intuition
To concatenate an array with itself, we need to create a new array that contains all elements of the original array twice, maintaining the same order. The elements at indices 0 to n-1 indices are followed by the same elements at indices n to 2n-1 


Algorithm
Initialize an empty result list or an array ans of size 2n, where n is the length of the input array.
Use a loop that runs twice.
Inside that loop, iterate through every element num in the input array nums.
Append num to the result list or assign it to the next available index in the result array.
Return the resulting array.

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            for num in nums:
                ans.append(num)
        return ans

Time & Space Complexity
Time complexity: 
O(n) where n is the length of the input array. We iterate through the array twice, performing 2n operations.
Space complexity: 
O(n) if we consider the space required for the output array of size 2n.


2. Iteration (One Pass)
Intuition

The problem defines the result array ans such that ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n. Instead of looping through the input twice, we can fill both required positions in the result array simultaneously while iterating through the input array just once. This utilizes the index mapping i and i + n directly.

Algorithm
Determine the length n of the input array.
Initialize a result array ans of size 2n.
Iterate through the input array nums using an index i from 0 to n - 1.
For each element at index i:
Set ans[i] = nums[i].
Set ans[i + n] = nums[i].
Return the resulting array.

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n)
        for i, num in enumerate(nums):
            ans[i] = ans[i + n] = num
        return ans


Time & Space Complexity

Time complexity: 
O(n) where  n is the length of the input array. Although we iterate through the input once, we still perform  2n total writes to the output array.
Space complexity: 
O(n) as we must allocate an array of size 2n for the output.


Common Pitfalls

Incorrect Result Array Size
Allocating an array of size n instead of 2n causes an index out of bounds error when writing to the second half.

# Wrong
ans = [0] * n

# Correct
ans = [0] * (2 * n)

Off-by-One When Using Index Offset
When using the one-pass approach with ans[i + n] = nums[i], forgetting that indices are zero-based or miscalculating the offset leads to incorrect placement of elements in the second half.