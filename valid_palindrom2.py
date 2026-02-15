# The brute force solution uses this by removing element one by one and then chek if its palindome or not it will take O(n**2) time complexity

# THIS SOULTION UTILIZES TIME COMPLEXITY O(N) AND SPACE COMPLEXIY O(N)
# because of the is two new sub arrays we have created we can totally avoid  by using helper func 
#--------------------------------------------------------------------
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r = 0 , len(s)-1
        while l<r:
            if s[l] != s[r]:
                skipL, skipR = s[l+1,r+1] ,s[l:r]
                return (skipL == skipL[::-1] 
                        or skipR == skipR[::-1])
            l,r = 1+1 , r-1
        return True
#------------------------------------------------------------------------------------------------

# THIS SOULTION UTILIZES TIME COMPLEXITY O(N) AND SPACE COMPLEXIY O(1)
# what we have done is that created a function so that it can cehck the plaindrome of it
#------------------------------------------------------------------------------------------------
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return (is_palindrome(l + 1, r) or
                        is_palindrome(l, r - 1))
            l += 1
            r -= 1

        return True
#------------------------------------------------------------------------------------------------


# Prerequisites
# Before attempting this problem, you should be comfortable with:

# Two Pointers Technique - Using pointers from both ends of a string to compare characters
# Palindrome Fundamentals - Understanding how to check if a string reads the same forwards and backwards
#---------------------------------------------------------------------------------------------------------
# Only Trying One Deletion Option
# When a mismatch is found at positions l and r, you must check both possibilities: removing the character at l or removing the character at r. A common mistake is only trying one option (like always removing the left character). Both substrings s[l+1...r] and s[l...r-1] must be checked, and the answer is true if either forms a palindrome.

# Forgetting That Zero Deletions Is Valid
# The problem asks if the string can become a palindrome by deleting at most one character. This includes deleting zero characters. If the original string is already a palindrome, the answer is true. Some solutions only consider the deletion case and forget to check if the string is already valid as-is.
