class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for ops in operations:
            if ops == "+":
                stack.append(stack[-1] + stack[-2])
            elif ops == "D":
                stack.append(2*stack[-1])
            elif ops == "C":
                stack.pop()
            else:
                stack.append(int(ops))
    
        return sum(stack)

# Common Pitfalls
# Forgetting to Convert String to Integer
# When the operation is a number, it comes as a string. Forgetting to parse it as an integer causes type errors or incorrect arithmetic.

# # Wrong: pushing string instead of integer
# stack.append(op)  # op is "5", not 5
# Accessing Stack Elements in Wrong Order for "+"
# The + operation requires adding the last two scores. When popping, the first pop gives the most recent score, and the second pop gives the one before it. Getting this order confused can lead to wrong results when the operation depends on position.
# Time & Space Complexity
# Time complexity: 
# O(n)
# Space complexity: 
# O(n)