# Two pointers solution
# elegant approach: we compare each element with its predecessor. Since duplicates are consecutive in a sorted array, an element is unique if it differs from the one before it. We maintain a write pointer that only advances when we find a new unique value.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(1,len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                r+=1
        return l
# Prerequisites
# Before attempting this problem, you should be comfortable with:

# Two Pointers - Using a read pointer and write pointer to modify arrays in-place
# In-Place Array Modification - Overwriting elements without using extra space
# Sorted Array Properties - Understanding that duplicates are always adjacent in sorted arrays


# Time & Space Complexity
# Time complexity: O(n)
# Space complexity: O(1)


# Not Leveraging the Sorted Property
# The array is already sorted, meaning duplicates are always adjacent. Some solutions use a hash set or sort the array again, which wastes time and space. Since duplicates are consecutive, you only need to compare each element with its predecessor (or the last written element) to detect duplicates in O(1) space.

# Returning the Wrong Value
# The function should return the count of unique elements, not modify and return the array itself. Additionally, the returned length k means the first k elements of nums contain the unique values. Some solutions off-by-one error by returning l - 1 instead of l, or forget that the write pointer already represents the count of unique elements written.