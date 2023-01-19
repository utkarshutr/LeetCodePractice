# User function Template for python3

class Solution:
    def countPairs(self, n, arr, k):
        cnt = 0
        for i in range(n):
            arr[i] = (arr[i]) % k

        hash = [0]*k
        for i in range(n):
            hash[arr[i]] += 1

        for i in range(k):
            cnt += (hash[i] * (hash[i] - 1)) / 2

        return cnt

# code here


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = 1
    input1 = 3
    input2 = "3 7 11"
    input3 = 4
    for _ in range(t):
        n = int(input1)
        arr = list(map(int, input2.split()))
        k = int(input3)

        ob = Solution()
        print(ob.countPairs(n, arr, k))
# } Driver Code Ends
