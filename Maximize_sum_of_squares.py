# Intro:
# You are given two positive integers num and sum.

# A positive integer n is good if it satisfies both of the following:

# The number of digits in n is exactly num.
# The sum of digits in n is exactly sum.
# The score of a good integer n is the sum of the squares of digits in n.

# Return a string denoting the good integer n that achieves the maximum score. If there are multiple possible integers, return the maximum ​​​​​​​one. If no such integer exists, return an empty string.

# Example:
num = 2
su = 3
# Output: "30"

# Explanation:
# There are 3 good integers: 12, 21, and 30.
# The maximum score is 9, which is achieved by the good integer 30. Therefore, the answer is "30".
def main():
    if num * 9 < su:
        return ''

    s = ''
    while num > 0:
        if su - 9 > 0:
            s += '9'
            su -= 9
        else:
            s += str(su)
            su = 0
        num -= 1

    s += '0'*num
    return s