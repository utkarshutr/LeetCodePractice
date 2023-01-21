# User function Template for python3
import collections


class Solution():
    def maxWeightCell(self, N, Edge):
        if N <= 1:
            return 0

        sum_arr = [0 for i in range(N)]
        for i in range(N):
            if Edge[i] != -1:
                sum_arr[Edge[i]] += i

        max_sum = max(sum_arr)
        for i in range(N - 1, -1, -1):
            if sum_arr[i] == max_sum:
                return i


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    input1 = 5
    input2 = "3 -1 -1 -1 3"
    for _ in range(1):
        N = int(input1)
        Edge = [int(i) for i in input2.split()]
        obj = Solution()
        ans = obj.maxWeightCell(N, Edge)
        print(ans)

# } Driver Code Ends
