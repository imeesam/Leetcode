class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chatSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in chatSet:
                chatSet.remove(s[l])
                l+=1
            chatSet.add(s[r])
            res = max(res, r-l+1)
        return res 
    
# Sliding Window
# Intuition
# Instead of restarting at every index like brute force, we can keep one window that always has unique characters.
# We expand the window by moving the right pointer.
# If we ever see a repeated character, we shrink the window from the left until the duplicate is removed.
# This way, the window always represents a valid substring, and we track its maximum size.
# It's efficient because each character is added and removed at most once.

# Time & Space Complexity
# Time complexity: 
# O(n)
# Space complexity: 
# O(m)