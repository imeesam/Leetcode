class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] +=1
            if len(count) <=2:
                continue
            new_count = defaultdict(int)
            for n ,c in count.items():
                if c > 1:
                    new_count[n] = c-1  
            count = new_count

        res = []
        for n in count:  # as this a loop it will take O(n) time but nah here not it not gonna take becauswe we have only 2 or maybe 3 elements here
            if nums.count(n) > len(nums)//3: # here we gotta this nums.count() have O(1) time
                res.append(n)
        return  res

#  above solution uses hash map we can do this with the dictonary as well.
# which is given as follows 
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic = {}
        res = []
        n = len(nums) // 3
        
        for n in nums:
            dic[n] = dic.get(n, 0) + 1
        
        for key, value in dic.items():
            if value > n:
                res.append(key)
        
        return res
