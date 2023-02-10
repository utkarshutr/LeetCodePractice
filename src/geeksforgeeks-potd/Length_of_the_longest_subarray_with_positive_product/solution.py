class Solution:
    def maxLength(self, arr, n):
        positive_len, negative_len, ans = 0, 0, 0
        for i in arr:
            if i == 0:
                positive_len = negative_len = 0

            elif i < 0:
                positive_len, negative_len = negative_len + 1 if negative_len else 0, positive_len + 1

            else:
                positive_len, negative_len = positive_len + 1, negative_len + 1 if negative_len else 0

            ans = max(ans, positive_len)

        return ans


if __name__ == '__main__':

    input1 = ["5"]
    input2 = ["1 -2 3 -4 -1"]
    for in1, in2 in zip(input1, input2):
        n = int(in1)
        arr = [int(x) for x in in2.strip().split()]
        obj = Solution()
        print(obj.maxLength(arr, n))
