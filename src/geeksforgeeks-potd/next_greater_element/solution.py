# User function Template for python3


class Solution:
    def nextLargerElement(self, arr, n):
        a = []
        result = [0] * n
        for i in range(n - 1, -1, -1):
            while a and a[-1] <= arr[i]:
                a.pop()
            if a:
                result[i] = a[-1]
            a.append(arr[i])
        for i in range(n):
            if result[i] == 0:
                result[i] = -1
        return result


# {
# Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = 1
    input1 = 4
    input2 = "1 3 2 4"
    for cases in range(test_cases):
        n = int(input1)

        a = list(map(int, input2.strip().split()))
        obj = Solution()
        res = obj.nextLargerElement(a, n)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()
# } Driver Code Ends
