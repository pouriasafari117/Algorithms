# Intro : 
# You are given an array nums of distinct positive integers. You need to sort the array in increasing order based on the sum of the digits of each number. If two numbers have the same digit sum, the smaller number appears first in the sorted order.
# Return the minimum number of swaps required to rearrange nums into this sorted order.
# A swap is defined as exchanging the values at two distinct positions in the array.

# Example 1:
nums = [37,100]
# Output: 1
# Explanation:
# Compute the digit sum for each integer: [3 + 7 = 10, 1 + 0 + 0 = 1] → [10, 1]
# Sort the integers based on digit sum: [100, 37]. Swap 37 with 100 to obtain the sorted order.
# Thus, the minimum number of swaps required to rearrange nums is 1.


# Example 2:
nums = [22,14,33,7]
nums = [18,43,34,16]
# Output: 0
# Explanation:
# Compute the digit sum for each integer: [2 + 2 = 4, 1 + 4 = 5, 3 + 3 = 6, 7 = 7] → [4, 5, 6, 7]
# Sort the integers based on digit sum: [22, 14, 33, 7]. The array is already sorted.
# Thus, the minimum number of swaps required to rearrange nums is 0.
se = {}
se1 = {}
for i in range(len(nums)):
    se1[nums[i]] = i
    if nums[i] in se:
        continue
    else:
        se[nums[i]] = 0
        for l in str(nums[i]): 
            se[nums[i]] += int(l)

print(se , se1)


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
        if se[a[x]] < se[b[y]]:
            final.append(a[x])
            x += 1

        elif se[a[x]] == se[b[y]]:
            if a[x] > b[y]:
                final.append(b[y])
                y += 1
            else:
                final.append(a[x])
                x += 1  

        else:
            final.append(b[y])
            y += 1

    final += a[x:]
    final += b[y:]

    return final

action = 0
x = main_sort_func(nums)
for i in range(len(x)):
    if i != se1[x[i]]:
        action += 1
print(x)
print(action)