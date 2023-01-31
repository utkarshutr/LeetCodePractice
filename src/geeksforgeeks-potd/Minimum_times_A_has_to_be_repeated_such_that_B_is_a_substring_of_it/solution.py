# User function Template for python3

class Solution:
    def minRepeats(self, A, B):
        # code here
        a = set(A)
        b = set(B)
        if b.issubset(a):
            temp_str = ""
            ans = 0
            while len(temp_str) < len(B):
                temp_str += A
                ans += 1
            if B in temp_str:
                return ans
            elif B in temp_str + A:
                return ans + 1
            else:
                return -1
        else:
            return -1


if __name__ == '__main__':
    input1 = ["abcd"]
    input2 = ["cdabcdab"]
    for in1, in2 in zip(input1, input2):
        A = in1
        B = in2

        ob = Solution()
        print(ob.minRepeats(A, B))
