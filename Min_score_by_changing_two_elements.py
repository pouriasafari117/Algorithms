# intro:
# you are given an integer array nums.
# The low score of nums is the minimum absolute difference between any two integers.
# The high score of nums is the maximum absolute difference between any two integers.
# The score of nums is the sum of the high and low scores.
# Return the minimum score after changing two elements of nums.
 
# Example 1:
# Input:
nums = [1, 4, 7, 8, 5]
nums = [59,27,9,81,33]
# Output: 3
# Explanation:
# Change nums[0] and nums[1] to be 6 so that nums becomes [6,6,7,8,5].
# The low score is the minimum absolute difference: |6 - 6| = 0.
# The high score is the maximum absolute difference: |8 - 5| = 3.
# The sum of high and low score is 3.

# Example 2:
# Input:
nums = [58,42,8,75,28]
# Output: 0
# Explanation:
# Change nums[1] and nums[2] to 1 so that nums becomes [1,1,1].
# The sum of maximum absolute difference and minimum absolute difference is 0.

def main1():
    nums.sort()
    return min(nums[-1] - nums[2] , nums[-3] - nums[0] , nums[-2] - nums[1])

def main2():
    if len(nums) <= 3:
        return 0
    
    mix1 = float('-inf')
    man1 = float('inf')
    man2 = float('inf')
    man3 = float('inf')

    for i in range(len(nums)):
        if mix1 < nums[i]:
            mix1 = nums[i]

        if man1 > nums[i]:
            man3 = man2
            man2 = man1
            man1 = nums[i]
        elif man2 > nums[i]:
            man3 = man2
            man2 = nums[i]
        elif man3 > nums[i]:
            man3 = nums[i]
    
    mix1_1 = float('-inf')
    mix1_2 = float('-inf')
    mix1_3 = float('-inf')
    man1_1 = float('inf')

    for i in range(len(nums)):
        if mix1_1 < nums[i]:
            mix1_3 = mix1_2
            mix1_2 = mix1_1
            mix1_1 = nums[i]
        elif mix1_2 < nums[i]:
            mix1_3 = mix1_2
            mix1_2 = nums[i]
        elif mix1_3 < nums[i]:
            mix1_3 = nums[i]

        if man1_1 > nums[i]:
            man1_1 = nums[i]

    x1 = mix1 - man3
    x2 = mix1_3 - man1_1
    x3 = mix1_2 - man2

    if x1 < x2 and x1 < x3:
        return x1
    elif x2 < x1 and x2 < x3:
        return x2
    return x3

print(main1() , main2())