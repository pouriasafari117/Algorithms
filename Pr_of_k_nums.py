# Intro:
# Design an algorithm that accepts a stream of integers and retrieves the product of the last k integers of the stream.
# Implement the ProductOfNumbers class:
# ProductOfNumbers() Initializes the object with an empty stream.
# void add(int num) Appends the integer num to the stream.
# int getProduct(int k) Returns the product of the last k numbers in the current list. You can assume that always the current list has at least k numbers.
# The test cases are generated so that, at any time, the product of any contiguous sequence of numbers will fit into a single 32-bit integer without overflowing.

# Example:
commands = ["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
values = [[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]
# Output
# [null,null,null,null,null,null,20,40,0,null,32]

# Explanation
# ProductOfNumbers productOfNumbers = new ProductOfNumbers();
# productOfNumbers.add(3);        // [3]
# productOfNumbers.add(0);        // [3,0]
# productOfNumbers.add(2);        // [3,0,2]
# productOfNumbers.add(5);        // [3,0,2,5]
# productOfNumbers.add(4);        // [3,0,2,5,4]
# productOfNumbers.getProduct(2); // return 20. The product of the last 2 numbers is 5 * 4 = 20
# productOfNumbers.getProduct(3); // return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
# productOfNumbers.getProduct(4); // return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
# productOfNumbers.add(8);        // [3,0,2,5,4,8]
# productOfNumbers.getProduct(2); // return 32. The product of the last 2 numbers is 4 * 8 = 32 


class ProductOfNumbers:

    def __init__(self):
        self.stream = []
        self.zero = -1

    def add(self, num: int) -> None:
        if num == 0:
            self.stream.append(0)
            self.zero = len(self.stream) - 1

        elif not self.stream or self.stream[-1] == 0:
            self.stream.append(num)

        else:
            self.stream.append(num * self.stream[-1])

    def getProduct(self, k):
        s= len(self.stream) - k

        if s <= self.zero:
            return 0

        if s == 0 or self.stream[s - 1] == 0:
            return self.stream[-1]
        return self.stream[-1] // self.stream[s - 1]

def main():
    x = ProductOfNumbers()
    res = [None]
    for i in range(1 , len(values)):
        if commands[i] == 'add':
            res.append(x.add(values[i][0]))
        else:
            res.append(x.getProduct(values[i][0]))
    return res
print(main())