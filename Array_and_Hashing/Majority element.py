class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        res, CountMax = 0 , 0 
        for n in nums:
            count[n] = 1 + count.get(n,0)
            res = n if count[n] > CountMax else res
            CountMax = max(count[n], CountMax)
        return res 
        
        # worst soluton 
