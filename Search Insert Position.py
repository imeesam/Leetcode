class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = 0 , len(nums)-1
        while l<=r:
            mid = l+ ((r-l)//2)
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                    l= mid+1
            else:
                 r=mid-1
        return l

# Prerequisites
# Before attempting this problem, you should be comfortable with:

# Arrays - Understanding how to traverse and access elements by index
# Binary Search - Knowing how to efficiently search in a sorted array by repeatedly halving the search space

# Time & Space Complexity
# Time complexity: 
# O(logn)
# Space complexity: 
# O(1) extra space.

# Common Pitfalls
# Off-by-One Errors in Binary Search Boundaries
# A frequent mistake is using incorrect loop conditions or boundary updates. Using l < r instead of l <= r (or vice versa) without adjusting the logic accordingly can cause the algorithm to miss elements or enter infinite loops. Similarly, setting r = mid instead of r = mid - 1 in certain variants can lead to incorrect results or infinite loops.

# Forgetting to Handle the "Insert at End" Case
# When the target is larger than all elements in the array, the insertion position should be n (the length of the array). Beginners often forget to account for this case, either returning -1, causing an index out of bounds error, or returning the last index incorrectly. Always ensure your algorithm correctly returns n when the target exceeds all array elements.