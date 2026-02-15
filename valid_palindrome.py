# knida cheating solution (using built in functions)
#---------------------------------------------------------------------
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]
#---------------------------------------------------------------------
# time and space complexity is O(n) because using extra memory and onepass

# builting functions
#---------------------------------------------------------------------
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1
        while l < r:
            while l < r and not self.alphanum(s[l]):
                l+=1
            while r > l and not self.alphanum(s[r]):
                r-=1
                
            if s[l].lower() != s[r].lower() :
                return False
            l , r = l+1 , r-1
        return True

    def alphanum(self,c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
#---------------------------------------------------------------------
# time and space complexity is O(n) because using extra memory and onepass

# Common Pitfalls
# Not Skipping Non-Alphanumeric Characters
# The problem requires ignoring all characters that are not letters or digits. Forgetting to skip spaces, punctuation, and special characters will cause false negatives. For example, "A man, a plan, a canal: Panama" should be recognized as a palindrome, but including the spaces and punctuation in the comparison will incorrectly return false.

# Case Sensitivity
# Letters must be compared in a case-insensitive manner. Comparing 'A' directly with 'a' will return false even though they should be treated as equal. Always convert both characters to the same case (lowercase or uppercase) before comparing.