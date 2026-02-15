class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0 
        prefixSum = {0:1} #  done for the edge case 
        for n in nums:
            curSum += n
            diff = curSum -k
            res+= prefixSum.get(diff,0)

            prefixSum[curSum] = 1+prefixSum.get(curSum,0)
        return res
    

# Prefix Sums - The optimal solution relies on the property that subarray sums can be computed as differences of prefix sums.
# Hash Maps - Used to store prefix sum frequencies for O(1) lookups when searching for complement values.
# the soultion is O(n) time complexity # space complexity O(n)

#Common Pitfalls
# Forgetting to Initialize the Hash Map with Zero
# The hash map must start with {0: 1} to handle subarrays that start from index 0. Without this initialization, subarrays where prefixSum == k from the beginning will not be counted.

# Attempting to Use Sliding Window
# Unlike the product variant, this problem allows negative numbers, which means the running sum is non-monotonic. Sliding window does not work here because shrinking the window might increase or decrease the sum unpredictably. The prefix sum + hash map approach is required.

# Updating the Hash Map Before Checking
# The order of operations matters. You must first check if curSum - k exists in the hash map, then add curSum to the map. Reversing this order would incorrectly count the current element as a valid "previous" prefix sum, leading to wrong results.