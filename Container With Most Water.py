# BRUTE FORCE O(n^2) solutions
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0

        for l in range(len(height)):
            for r in range(l+1,len(height)):
                area = (r-l)* min(height[l],height[r])
                res = max(res,area)
        
        return area 
    # this ant gonna work on leetcode time will exceed 
# this is how it works
# 1. Brute Force
# Intuition
# We try every possible pair of lines and compute the area they form.
# For each pair (i, j), the height of the container is the shorter of the two lines, and the width is the distance between them.
# By checking all pairs, we are guaranteed to find the maximum area.

# Algorithm
# Initialize res = 0 to track the maximum area found.
# Use two nested loops:
# Outer loop picks the left line i.
# Inner loop picks the right line j > i.
# For each pair (i, j):
# Compute the height as min(heights[i], heights[j]).
# Compute the width as j - i.
# Update res with the maximum of its current value and the new area.
# After checking all pairs, return res.
# Time & Space Complexity
# Time complexity: 
# O(n2)
# Space complexity:
# O(1)

# Two pointer solutions O(n) linear time:
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l,r = 0,len(height)-1
        while l<r:
            area = (r-l)* min(height[l],height[r])
            res = max(res,area)  
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return area 
# this solution is o(1) for space and for time complexity it is o(n)
# Using two pointers lets us efficiently search for the maximum area without checking every pair.
# We start with the widest container (left at start, right at end).
# The height is limited by the shorter line, so to potentially increase the area, we must move the pointer at the shorter line inward.
# Moving the taller line never helps because it keeps the height the same but reduces the width.
# By always moving the shorter side, we explore all meaningful possibilities.

# Common Pitfalls
# Moving the Wrong Pointer
# The algorithm requires moving the pointer at the shorter height inward. Moving the taller pointer instead never increases the area (since height is limited by the shorter side) and can cause the algorithm to miss the optimal solution.

# Confusing This Problem with Trapping Rain Water
# Unlike the Trapping Rain Water problem where you need to sum water trapped between bars, this problem finds a single container formed by two lines. Applying the wrong mental model leads to incorrect area calculations.

# Off-by-One Errors in Width Calculation
# The width between indices l and r is r - l, not r - l + 1. Using the wrong formula overestimates the area by one unit for every pair, leading to incorrect results.