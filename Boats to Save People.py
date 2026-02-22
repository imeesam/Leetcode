# two pointers solution
# 1. Sorting + Two Pointers
# Intuition
# Since each boat can carry at most two people and has a weight limit, we want to pair the heaviest person with the lightest person when possible. By sorting the weights, we can use two pointers: one at the heaviest person and one at the lightest. If they can share a boat, we move both pointers; otherwise, the heaviest person takes a boat alone.
# Algorithm
# Sort the people array in ascending order.
# Initialize two pointers: left at index 0, right at the last index.
# Initialize a boat counter to 0.
# While left is less than or equal to right:
# Calculate the remaining capacity after placing the heaviest person (at right).
# Decrement right and increment the boat count.
# If the lightest person (at left) fits in the remaining capacity and left is still valid, increment left.
# Return the boat count.

# Time & Space Complexity
# Time complexity:
# O(nlogn)
# Space complexity:
# O(1) or O(n) depending on the sorting algorithm.

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0  # boats for the people
        l , r = 0 , len(people)-1
        while l<=r:
            remain = limit - people[r] # calculate remaining weight on boat
            r-=1
            res+=1 # increase boat counter
            if l<=r and remain >= people[l]:  # checking if there person left and if the remaing weights is greater than person on
                l+=1
        return res

# Common Pitfalls
# Forgetting to Sort the Array First
# The two-pointer approach only works on sorted arrays. Attempting to pair people without sorting will not produce the minimum number of boats because you cannot guarantee pairing the heaviest with the lightest.

# Trying to Fit More Than Two People per Boat
# The problem states each boat can carry at most 2 people, regardless of weight. A common mistake is trying to fit three or more light people in one boat.

# # Wrong: trying to fit multiple light people
# while l <= r and remain >= people[l]:
#     remain -= people[l]
#     l += 1  # Might add more than 2 people total
# Not Moving the Right Pointer First
# The heaviest person always needs a boat. A mistake is checking if the lightest person fits first, which can lead to incorrect pointer movement when the lightest person alone exceeds the remaining capacity.