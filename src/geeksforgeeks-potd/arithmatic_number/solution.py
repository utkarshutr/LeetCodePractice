"""
The nth term (B) would be -> B = A + (n * C)
        We have A, B and C as input, so -> n = (B - A) / C

        Now, we just need to check if B-A can be fully divisible by C and the value of n should always be greater then 1

"""


class Solution:
    def inSequence(self, A, B, C):
        # if C is 0, means only 1 element.
        if C == 0:
            return 1 if A == B else 0
        if B == A:
            return 1

        return 1 if ((B - A) % C) == 0 and ((B - A) / C) >= 1 else 0


if __name__ == '__main__':
    input1 = ["1 3 2", "1 2 3", "10 10 42"]
    for in1 in input1:
        A, B, C = [int(x) for x in in1.split()]

        ob = Solution()
        print(ob.inSequence(A, B, C))
