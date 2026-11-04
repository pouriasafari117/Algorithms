# Intro:
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
# string convert(string s, int numRows);

# Example 1:
s = "PAYPALISHIRING"
numRows = 3
# Output: "PAHNAPLSIIGYIR"

# Example 2:
s = "PAYPALISHIRING"
numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

# Example 3:
s = "A"
numRows = 1
# Output: "A"
def main():
    if numRows == 1:
        return s
    if len(s) <= numRows:
        return s

    mix = 2*(numRows - 1)
    moves = [(mix - 2*i , 2*i) for i in range(numRows)]
    # return moves

    print(moves)

    i = 0
    res = ''
    while i < 4:
        j = i
        res += s[i]
        act = moves[i]
        step = 0
        while j < len(s):
            if act[step] == 0:
                if step == 0:
                    step += 1
                else:
                    step = 0
                continue
            
            if step == 0:
                j += act[step]
                if not j < len(s):
                    continue
                res += s[j]
                step += 1
                            
            else:
                j += act[step]
                if not j < len(s):
                    continue
                res += s[j]
                step = 0

            print(res , i , j)
            # break
        i += 1

    return res
print(main())