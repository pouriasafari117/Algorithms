s = "(abcd)"

class Q:
    def __init__(self):
        self.q_lis = []

    def nq(self , a):
        self.q_lis.append(a)

    def dq(self):
        return self.q_lis.pop(0)

class Stack:
    def __init__(self):
        self.s_lis = []

    def pus(self , a):
        self.s_lis.append(a)

    def po(self):
        return self.s_lis.pop()

def m(s1):
    s = Stack()
    q = Q()

    for i in s1:
        if i == ')':
            poi = s.po()
            while poi != '(':
                q.nq(poi)
                poi = s.po()

            while len(q.q_lis) > 0:
                s.pus(q.dq())

        else:
            s.pus(i)
        print(q.q_lis , s.s_lis)

    string = ''
    # print(s.s_lis)
    while len(s.s_lis) > 0:
        string += s.po()

    string2 = ''
    for i in range(len(string)-1 , -1 , -1):
        string2 += string[i]
    return string2

print(m(s))