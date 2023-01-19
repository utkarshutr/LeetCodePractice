# User function Template for python3

import collections


class Solution:
    def minIncrements(self, arr, N):
        count = collections.Counter(arr)
        dup_val_list = []
        unique_elements_list = []

        min_increment = 0
        process_counter = 0

        for i in range(1, 1000000):
            if count[i] >= 2:
                dup_val_list.extend([i] * (count[i] - 1))
                process_counter += 1
            elif count[i] == 1:
                process_counter += 1
            elif count[i] == 0:
                unique_elements_list.append(i)
                if dup_val_list:
                    min_increment += unique_elements_list.pop() - dup_val_list.pop()
                    process_counter += 1

            if process_counter == N:
                break

        return min_increment


# Code here


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':

    T = 1
    input1 = 3
    input2 = "1 2 2"
    while T > 0:
        # N=int(input())
        N = input1
        # arr = [int(i) for i in input().split()]
        arr = [int(i) for i in input2.split()]
        ob = Solution()
        print(ob.minIncrements(arr, N))

        T -= 1
# } Driver Code Ends
