from typing import List


class Solution:
    def solve(self, N: int, K: int, arr: List[int]) -> int:
        sum_array = sum(arr)
        gcds_of_sum = []
        m = int(sum_array ** 0.5)
        for i in range(1, m + 1):
            if sum_array % i == 0:
                gcds_of_sum.append(i)
                if i != (sum_array // i):
                    gcds_of_sum.append(sum_array // i)

        gcds_of_sum.sort(reverse=True)
        for i in range(1, N):
            arr[i] += arr[i - 1]

        out = 1
        for x in gcds_of_sum:
            cnt = 0
            for y in arr:
                if y % x == 0:
                    cnt += 1
            if cnt >= K:
                out = x
                break

        return out


# {
# Driver Code Starts

input1 = 5
input2 = 4
input3 = "6 7 5 27 3"


class IntArray:
    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input3.strip().split()]  # array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = 1

    for _ in range(t):
        N = input1
        K = input2
        arr = IntArray().Input(N)

        obj = Solution()
        res = obj.solve(N, K, arr)

        print(res)

# } Driver Code Ends
