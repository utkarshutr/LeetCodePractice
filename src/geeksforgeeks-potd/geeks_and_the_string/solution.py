# User function Template for python3

class Solution:

    # Function to remove pair of duplicates from given string using Stack.
    def removePair(self, s):
        stack = []

        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)

        if not stack:
            return "-1"

        return "".join(stack)


if __name__ == '__main__':
    test_cases = 1
    input1 = "aaabbaaccd"
    for cases in range(test_cases):
        obj = Solution()
        print(obj.removePair(str(input1)))
