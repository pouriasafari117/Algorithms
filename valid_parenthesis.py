# intro:

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


class Stack:
    def __init__(self):
        self.s_lis = []

    def pus(self , a):
        self.s_lis.append(a)

    def po(self):
        return self.s_lis.pop()

def asli(s = '([)]'):
        st = Stack()

        for i in s:
            if i == '(' or i == '[' or i == '{':
                st.pus(i)
                continue

            if st.s_lis == []:
                return False

            elif i == ')':
                if st.po() == '(':
                    continue
            elif i == ']':
                if st.po() == '[':
                    continue
            else:
                if st.po() == '{':
                    continue

            return False
        if st.s_lis == []:
            return True
        return False
print(asli())