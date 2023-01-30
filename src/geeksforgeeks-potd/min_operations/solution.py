class Solution:
    def solve(self, a: int, b: int) -> int:
        if a == b:
            return 0

        if a == 0 or b == 0:
            return 1

        a_and_b = a & b
        if a_and_b == a or a_and_b == b:
            return 1

        return 2


if __name__ == "__main__":
    input1 = [5, 100, 94]
    input2 = [12, 100, 8]
    for input in zip(input1, input2):
        a = int(input[0])
        b = int(input[1])
        obj = Solution()
        res = obj.solve(a, b)

        print(res)
