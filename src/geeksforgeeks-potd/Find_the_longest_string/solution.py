# User function Template for python3


class Solution():
    def longestString(self, arr, n):
        # your code goes here
        # traversed_list = []
        result_list_index = -1
        result_list = []

        for i in range(n):
            sub = ""
            to_add = True
            for e in arr[i]:
                sub = sub + e
                if not sub in arr:
                    to_add = False
                    break
            if to_add:
                result_list_index = i
                result_list.append(arr[i])

        print(result_list)
        if result_list_index == -1:
            return ""
        else:
            max_len = 0
            result_ele = -1
            for ele in result_list:
                if max_len == len(ele) and ele < result_ele:
                    result_ele = ele
                elif len(ele) > max_len:
                    max_len = len(ele)
                    result_ele = ele

            return result_ele

    # {


# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    # for _ in range(int(input())):
    #     n = int(input())
    #     arr = [i for i in input().split()]
    s = "llw lc ls llj ls t l ll llp llq y d"
    arr = s.split(" ")
    n = 12
    print(Solution().longestString(arr, n))
# } Driver Code Ends
