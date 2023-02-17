"""
Approach:

1) we will first get the sum of first Kth elements.
2) Once we are on k+1th element, we will append the sum to the list.
    - to calculate the updated sum, we reduce the sum by kth previous element.
    - and add the current element
"""
class Solution():
    def solve(self, N, K, GeekNum):
        sum = 0
        for i in range(N):
            if i >= K:
                GeekNum.append(sum)
                sum -= GeekNum[i-K]

            sum += GeekNum[i]

        return GeekNum[-1]

if __name__ == "__main__":
    input1 = ["6 1", "5 3"]
    input2 = ["4", "0 1 2"]
    for in1, in2 in zip(input1, input2):
        N, K = map(int, in1.split())
        GeekNum = [int(i) for i in in2.split()]
        print(Solution().solve(N, K, GeekNum))
