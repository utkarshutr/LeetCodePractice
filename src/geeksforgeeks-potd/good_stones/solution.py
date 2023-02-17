class Solution:
    def goodStones(self, n, arr) -> int:
        visited = [0] * n

        def dfs(i):

            nonlocal arr, visited, n
            if i < 0 or i >= n:
                return True

            if visited[i] > 0:
                return visited[i] == 2

            visited[i] = 1
            if dfs(i + arr[i]):
                visited[i] = 2
                return True
            return False

        return sum(dfs(i) for i in range(n))


if __name__ == "__main__":
    input1 = ["7", "6"]
    input2 = ["2 3 -1 2 -2 4 1", "1 0 -3 0 -5 0"]
    for in1, in2 in zip(input1, input2):
        n = int(in1)
        arr = list(map(int, in2.split()))
        obj = Solution()
        print(obj.goodStones(n, arr))
