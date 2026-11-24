# Intro:
# You are given an array of positive integers nums.
# An array arr is called product equivalent if prod(arr) == lcm(arr) * gcd(arr), where:
# prod(arr) is the product of all elements of arr.
# gcd(arr) is the GCD of all elements of arr.
# lcm(arr) is the LCM of all elements of arr.
# Return the length of the longest product equivalent subarray of nums.

# Example 1:
nums = [1, 2, 1, 2, 1, 1, 1]
# Output: 5
# Explanation: 
# The longest product equivalent subarray is [1, 2, 1, 1, 1], where prod([1, 2, 1, 1, 1]) = 2, gcd([1, 2, 1, 1, 1]) = 1, and lcm([1, 2, 1, 1, 1]) = 2.

# Example 2:
nums = [2, 3, 4, 5, 6]
# Output: 3
# Explanation: 
# The longest product equivalent subarray is [3, 4, 5].

# Example 3:
# nums = [1, 2, 3, 1, 4, 5, 1]
# Output: 5

import math
def main(n):
    mix = float('-inf')
    for i in range(len(n)):
        gcd = n[i]
        pr = n[i]
        lcm = n[i]
        for l in range(i+1 , len(n)):
            # print(n[i:l+1])
            pr *= n[l]
            gcd = math.gcd(gcd, n[l])
            lcm = (lcm * n[l]) // math.gcd(lcm, n[l])
            if pr == gcd * lcm:
                if mix < l-i+1:
                    # print(pr , gcd , lcm , mix , n[i:l+1])
                    mix = l-i+1
    return mix

print(main(nums))