class Solution:
    def distinctColoring(self, N, r, g, b):
        rc, gc, bc = 0, 0, 0

        for i in range(N):
            nrc = r[i] + min(gc, bc)
            ngc = g[i] + min(rc, bc)
            nbc = b[i] + min(rc, gc)
            rc, gc, bc = nrc, ngc, nbc

        return min(rc, gc, bc)


if __name__ == '__main__':
    input_N = [3]
    input_r = ["1 1 1"]
    input_g = ["2 2 2"]
    input_b = ["3 3 3"]
    for in_N, in_r, in_g, in_b in zip(input_N, input_r, input_g, input_b):
        N = in_N
        r = list(map(int, in_r.split()))
        g = list(map(int, in_g.split()))
        b = list(map(int, in_b.split()))

        ob = Solution()
        print(ob.distinctColoring(N, r, g, b))
