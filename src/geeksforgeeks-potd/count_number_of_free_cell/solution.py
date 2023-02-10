"""
Approach:
The idea is, to keep track of rows and columns we have visited.
after visiting any row and column, we can calculate total number of remaining one's
        calculation is simple ->
                (number of rows and columns total we visited) *n -> returns total 1s but some are duplicates
                to remove the duplicate counting, we just have to remove the cross of rows and columns

        once we get number of one's, subtract it from number of zero's, and you get your answer

"""
class Solution():
    def countZero(self, n, k, arr):
        row_set, col_set = set(), set()
        total_zero = n * n

        def zeros(rs_len, cs_len):
            total_one = ((rs_len + cs_len) * n) - (rs_len * cs_len)
            return total_zero - total_one

        ans = []
        for r, c in arr:
            row_set.add(r)
            col_set.add(c)
            ans.append(zeros(len(row_set), len(col_set)))

        return ans


input1 = ["3 3"]  # n=matrix size(n*n), k=integer - number of tasks
input2 = [["2 2", "2 3", "3 2"]]  # tasks to be completed. "row column"
for in1, in2 in zip(input1, input2):
    n, k = map(int, in1.split())
    arr = []
    for i in range(k):
        x, y = map(int, in2[k].split())
        arr.append([x, y])
    obj = Solution()
    res = obj.countZero(n, k, arr)
    for i in res:
        print(i, end=" ")
    print()
# } Driver Code Ends
