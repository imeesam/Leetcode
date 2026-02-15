# iterative solution
# ------------------------------------------------------------------
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l,r = 0, len(s)-1

        while l<r:
            s[l] ,s[r] = s[r],s[l]
            l,r = l+1, r-1
# time complexity of the soultion is 0(n) (due to iterative) and space complexity is O(1) (doing in place)
# ------------------------------------------------------------------

# stack solution
# ------------------------------------------------------------------
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        stack = []
        for c in s:
            stack.append(c)
        i = 0
        while stack:
            s[i] = (stack.pop())
            i+=1

# time complexity of the soultion is 0(n) (due to iterative) and space complexity is also O(n) (using place)
# ------------------------------------------------------------------

# Recursive solution
# ------------------------------------------------------------------
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def recursive(l,r):
            if l<r:
                s[l] , s[r] = s[r], s[l]
                recursive(l+1,r-1)
        recursive(0, len(s)-1)
# time complexity of the soultion is 0(n) (due to iterative) and space complexity is also O(n) (using recursion)
# ------------------------------------------------------------------

# Before attempting this problem, you should be comfortable with:

# Arrays - Basic array indexing and iteration
# Two Pointers - Using pointers at opposite ends to traverse and modify data
# In-place Modification - Modifying data structures without using extra space


# Common Pitfalls
# Using Incorrect Loop Termination Condition
# When using two pointers, the loop should terminate when l >= r, not when l > r. Using l != r works for odd-length strings but is less intuitive. The condition l < r correctly handles both even and odd length arrays.

# Returning a New String Instead of Modifying In-Place
# The problem requires modifying the input array in-place. A common mistake is creating a new reversed array or string and returning it, which violates the in-place requirement and uses unnecessary extra space.