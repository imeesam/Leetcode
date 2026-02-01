class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) =! len(t):
            return False
        
        # building hashmaps
        countS , countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(T[i],0)
        
        # # iterating hashmaps
        # for c in countS:
        #     if countS[c] != countT.get([c],0):
        #         return False
        # return True
        # or directly 
        if countS == countT:
            return True
        return False
        # this is one way to so this question through hashmap
# -----------------------------------------------------------------------
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        # this will wont work in interveiws as this is considered as cheating

# ------------------------------------------------------------------------
# using sorted function for it 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

