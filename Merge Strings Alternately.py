# using 2 pointer solution with o(n+m) tc and o(n+m)sc 
#--------------------------------------------------------------------------------------------------
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j = 0,0
        res  = []
        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i+=1
            j+=1
        res.append(word1[i:])
        res.append(word2[j:])
        return "".join(res)
#--------------------------------------------------------------------------------------------------

# there can be more solution to this that have same oc and tc 
# Prerequisites
# Before attempting this problem, you should be comfortable with:
# Strings - Understanding string indexing and character access
# Two Pointers - Using multiple indices to traverse data structures simultaneously
# StringBuilder / String Concatenation - Efficiently building strings in loops to avoid O(n^2) complexity

# Common Pitfalls
# Forgetting to Append the Remaining Characters
# When one string is longer than the other, the remaining characters must be appended after the alternating portion is complete. Stopping the loop when the shorter string ends without handling the leftover characters produces an incomplete result.

# Using String Concatenation in a Loop
# In many languages, repeatedly concatenating strings with + inside a loop creates a new string object each time, leading to O(n^2) time complexity. Use a StringBuilder, list of characters, or similar efficient structure to build the result, then join at the end.