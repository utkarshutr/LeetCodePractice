"""
The problem says that we can append a single character or an existing string.
So, we first need to find the biggest string which is duplicate in our string. The first loop finding the big duplicate
 string. Then we are just reducing the duplicate steps from total.

Please note - that question says we can only replace the string once. Other time, we can only append a single character.
"""

class Solution:
    def minOperation(self, s):
        big = ''
        s1 = ''
        for x in range(len(s)):
            s1 += s[x]
            if s1 in s[x + 1:]:
                big = s1
        if big:
            return len(s) - len(big) + 1
        return len(s)


if __name__ == '__main__':
    t = 1
    input1 = ["nrnrvynrnrvystmwcy", "yyyyyyyyyyyyyyyyyyyyyddtdgdt", "rtkrtkjrtkrtkjprepgg"]
    for input in input1:
        s = input
        ob = Solution()
        ans = ob.minOperation(s)
        print(ans)
