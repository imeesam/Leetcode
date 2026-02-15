class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping character count to the list of anagrams 
        for i in strs:
            count = [0] * 26  # a....z
            for c in i:
                count[ord(c)-ord('a')] +=1
            res[tuple(count)].append(i)
        return list(res.values())
# this is optimal solution of O(n*m)
            
