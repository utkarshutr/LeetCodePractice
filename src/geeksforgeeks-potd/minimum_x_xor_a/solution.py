# User function Template for python3

class Solution:
    def minVal(self, a, b):
        set_bits_b = bin(b)[2:].count('1')
        set_bits_a = bin(a)[2:].count('1')
        ans = 0
        for i in range(0, 32):
            mask = 1 << i
            set_bits = a & mask
            if set_bits == 0 and set_bits_b > set_bits_a:
                ans |= mask
                set_bits_b -= 1

            elif set_bits and set_bits_a > set_bits_b:
                set_bits_a -= 1
            else:
                ans |= set_bits

        return ans


if __name__ == '__main__':
    t = 1
    input1 = 3
    input2 = 5
    for i in range(t):
        a = input1
        b = input2

        ob = Solution()
        print(ob.minVal(a, b))
# } Driver Code Ends
