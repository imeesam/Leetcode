# three pointer soultions
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last =  m+n-1
        while m>0 and n>0:
            if nums1[m] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m-=1
            else:
                nums1[last] = nums2[n-1]
                n-=1

            last-=1
        
        while n>0:
            nums1[last] = nums2[n-1]
            n, last =  n-1 , last-1
# time complexity of this soultion is o(n) and space complexity is o(1) no extra space


# Prerequisites
# Before attempting this problem, you should be comfortable with:

# Arrays - Understanding how to access and modify elements by index
# Two Pointers - Traversing arrays from different directions simultaneously
# In-place Algorithms - Modifying data structures without using extra space

# Common Pitfalls
# Merging From the Front Instead of the Back
# When merging in place, starting from the front of nums1 overwrites elements that have not yet been processed. This destroys data you still need. Always merge from the back of nums1 where there is empty space, placing the largest elements first.

# Forgetting to Copy Remaining Elements From nums2
# After the main merge loop, if there are remaining elements in nums2, they must be copied to nums1. Elements remaining in nums1 are already in their correct positions, but leftover nums2 elements need explicit placement. Missing this step leaves the result incomplete.
        