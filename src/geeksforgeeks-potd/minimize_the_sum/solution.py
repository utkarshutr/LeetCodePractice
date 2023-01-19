# User function Template for python3

import heapq as hp


class Solution:
    def minimizeSum(self, N, arr):
        min_sum = 0
        hp.heapify(arr)

        while N > 1:
            t = hp.heappop(arr) + hp.heappop(arr)
            min_sum += t
            hp.heappush(arr, t)
            N -= 1

        return min_sum


# Code here


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = 1
    input1 = 5
    input2 = "1 3 7 5 6"

    for _ in range(t):
        # n = int(input())
        n = input1
        # A = [int(x) for x in input().split()]
        A = [int(x) for x in input2.split()]
        ob = Solution()
        print(ob.minimizeSum(n, A))
# } Driver Code Ends
