Description
You are given an array nums consisting of n elements where each element is an integer representing a color:

0 represents red
1 represents white
2 represents blue
Your task is to sort the array in-place such that elements of the same color are grouped together and arranged in the order: red (0), white (1), and then blue (2).

You must not use any built-in sorting functions to solve this problem.

Intuition
The Dutch National Flag algorithm partitions the array into three sections in a single pass. We maintain pointers for the boundary of 0s (left), the boundary of 2s (right), and the current element being examined. When we see a 0, we swap it to the left section. When we see a 2, we swap it to the right section. 1s naturally end up in the middle.

Algorithm
Initialize three pointers: l (boundary for 0s), i (current element), and r (boundary for 2s).
While i <= r:
If nums[i] is 0, swap with nums[l], increment both l and i.
If nums[i] is 2, swap with nums[r], decrement r (do not increment i since the swapped element needs to be checked).
If nums[i] is 1, just increment i.

Time & Space Complexity
Time complexity: O(n)
Space complexity: O(1)