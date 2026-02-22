class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a<0 and stack[-1]>0:
                diff = a+stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff>0:
                    a=0
                else:
                    a= 0
                    stack.pop()
            if a:
                stack.append(a)

        return stack

# Time & Space Complexity
# Time complexity: 
# O(n)
# Space complexity: 
# O(n)

# Common Pitfalls
# Assuming All Asteroids Collide
# Not all asteroids collide. Two asteroids moving in the same direction (both positive or both negative) never collide. A negative asteroid followed by a positive asteroid also never collide since they move apart.

# # Wrong: checking if signs differ without considering direction
# if asteroids[i] * asteroids[j] < 0:  # collision!
# # Right: collision only when positive is before negative
# if stack[-1] > 0 and a < 0:  # potential collision
# Forgetting Chain Reactions
# A single incoming asteroid can destroy multiple asteroids on the stack. You need a loop, not just a single comparison.

# # Wrong: only one comparison
# if stack and a < 0 and stack[-1] > 0:
#     # handle one collision and move on
# # Right: keep checking until no more collisions
# while stack and a < 0 and stack[-1] > 0:
#     # handle collision, may need to pop multiple times
# Incorrect Size Comparison
# When comparing asteroid sizes, remember that negative asteroids have negative values. Use absolute value for size comparison.

# # Wrong: comparing raw values
# if stack[-1] > a:  # incorrect when a is negative
# # Right: compare magnitudes
# if stack[-1] > abs(a):  # or equivalently: stack[-1] + a > 0