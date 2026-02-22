class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i ,t in enumerate(temperatures):
            while stack and  t>stack[-1][0]:
                stackT, stacki = stack.pop()
                res[stacki] =  (i-stacki)
            stack.append([t,i])
        return res


# Algorithm
# Create a result list filled with zeros.
# Use a stack to store pairs of (temperature, index) for days that haven't found a warmer day yet.
# Iterate through the temperature list:
# While the stack is not empty and the current temperature is warmer than the top of the stack:
# Pop the top element.
# Compute how many days passed and update the result.
# Push the current day onto the stack.
# Return the filled result list.



# Common Pitfalls
# Using Greater-Than-or-Equal Instead of Strictly Greater
# The problem asks for the next warmer day, meaning strictly greater temperature. Using >= instead of > causes the algorithm to stop at equal temperatures, producing incorrect results.

# # Wrong: stops at equal temperatures
# while stack and t >= stack[-1][0]:
#     # This pops when temperatures are equal, not just warmer

# # Correct: strictly greater
# while stack and t > stack[-1][0]:
#     stackT, stackInd = stack.pop()
#     res[stackInd] = i - stackInd
# Storing Only Indices Without Temperature Access
# When using a stack, you need to compare temperatures. Storing only indices works if you can access temperatures[index], but mixing up index and value access leads to comparison errors.

# # Correct: store just indices but access temperature via array
# stack = []  # stores indices
# for i, t in enumerate(temperatures):
#     while stack and t > temperatures[stack[-1]]:
#         idx = stack.pop()
#         res[idx] = i - idx
#     stack.append(i)
# Off-by-One Errors in Day Counting
# The result should be the number of days to wait, which is the difference in indices. Initializing count wrong or miscalculating the difference leads to off-by-one errors.

# # Wrong: starting count at 0
# count = 0
# j = i + 1
# while j < n and temperatures[j] <= temperatures[i]:
#     j += 1
#     count += 1  # count is now j - i - 1, off by one

# # Correct: difference of indices
# res[i] = j - i  # Direct index difference gives correct wait days