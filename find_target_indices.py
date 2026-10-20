# Intro
# You are given a 0-indexed integer array nums and a target element target.

# A target index is an index i such that nums[i] == target.

# Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

 

# Example 1:

nums = [1,2,5,2,3]
target = 2
# Output: [1,2]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The indices where nums[i] == 2 are 1 and 2.
# Example 2:

# Input: nums = [1,2,5,2,3], target = 3
# Output: [3]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The index where nums[i] == 3 is 3.

se = {-1 : 0 , 1 : 0}
for i in range(nums):
    if nums[i] < target:
        se[-1] += 1

    elif nums[i] > target:
        se[1] += 1


if se[-1] != 0 and se[1] != 0:
    lis = [i for i in range(se[-1] , len(nums) - se[1] - 1)]
