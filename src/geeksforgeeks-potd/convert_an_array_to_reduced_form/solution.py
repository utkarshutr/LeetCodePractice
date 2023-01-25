# User function Template for python3
class Solution:

    def convert(self, arr, n):
        arr_sorted = sorted(arr)
        ans = arr
        dict_indexed = {}
        for i in range(n):
            dict_indexed[arr_sorted[i]] = i

        for i in range(n):
            arr[i] = dict_indexed[arr[i]]


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = 1
    input1 = 5
    input2 = "5 10 40 30 20"
    while tc > 0:
        n = int(input1)
        arr = list(map(int, input2.strip().split()))
        ob = Solution()
        ob.convert(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends
