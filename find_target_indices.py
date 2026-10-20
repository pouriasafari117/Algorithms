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


def main_sort_func(a):
    if len(a) <= 1:
        return a

    mid = len(a) // 2
    left = main_sort_func(a[:mid])
    right = main_sort_func(a[mid:])

    return merge(left , right)

def merge(a , b):
    x = 0
    y = 0
    final = []
    while x < len(a) and y < len(b):
        if a[x] < b[y]:
            final.append(a[x])
            x += 1

        else:
            final.append(b[y])
            y += 1

    final += a[x:]
    final += b[y:]

    return final

k = main_sort_func(nums)

lis = []
flag = False
for i in range(len(k)):
    if k[i] < target:
        continue
    elif k[i] > target:
        break
    else:
        flag = True

    if flag:
        lis += [i]

print(lis)