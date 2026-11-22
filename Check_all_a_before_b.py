# Given a string s consisting of only the characters 'a' and 'b',
# return true if every 'a' appears before every 'b' in the string. Otherwise, return false.

# Example 1:
s = "aaabbb"
# Output: true
# Explanation:
# The 'a's are at indices 0, 1, and 2, while the 'b's are at indices 3, 4, and 5.
# Hence, every 'a' appears before every 'b' and we return true.

def main():
    for i in range(len(s)):
        if s[i] == 'b' and s[i+1] == 'a':
            return False
    return True