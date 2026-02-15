# kind of generic result
# because in this we are hardcoding variable

def concatenation(nums):
    arr = []
    for i in range(2):
        for n in nums:
            arr.append(n)
    return arr

#  what if interveiwer, ask that we are given a variable this is how we gonna do....

def concatenation(nums,x):
    arr = []
    for i in range(x):
        for n in nums:
            arr.append(n)
    return arr
