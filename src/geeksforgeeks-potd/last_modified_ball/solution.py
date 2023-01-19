#User function Template for python3

class Solution():
    def solve(self, N, A):
#your code here
        for count in range(N, 0, -1):
            if A[count-1] < 9:
                return count

#{
# Driver Code Starts
#Initial Template for Python 3

for _ in range(1):
    # n = input()
    n = 3
    input1 = "1 9 9"
    # array=[int(i) for i in input().split()]
    array=[int(i) for i in input1.split()]
    obj = Solution()
    print(obj.solve(n, array))
# } Driver Code Ends
