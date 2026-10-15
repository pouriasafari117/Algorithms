# Intro:
# You are given an integer array nums. You may rearrange the elements in any order.
# The alternating score of an array arr is defined as:
# score = arr[0]2 - arr[1]2 + arr[2]2 - arr[3]2 + ...
# Return an integer denoting the maximum possible alternating score of nums after rearranging its elements.
# Example 1:

nums = [1,2,3]
# Output: 12

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
        if abs(a[x]) < abs(b[y]):
            final.append(a[x])
            x += 1

        else:
            final.append(b[y])
            y += 1

    final += a[x:]
    final += b[y:]

    return final

nums = main_sort_func(nums)
# print(nums)

res = 0
r = len(nums)-1
l = 0
for i in range(len(nums)):
    if i % 2 == 0:
        res += (nums[r])**2
        r -= 1
    else:
        res -= (nums[l])**2
        l += 1

print(res)