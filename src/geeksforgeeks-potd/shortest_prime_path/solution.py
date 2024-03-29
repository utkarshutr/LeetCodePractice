from math import sqrt, ceil
from collections import defaultdict


class Solution:
    def __init__(self):
        N = 10000
        self.adjs = defaultdict(set)  # { num : set(num) }
        self.prime = [1 for i in range(N + 1)]
        self.prime[0] = self.prime[1] = 0
        # prime sieve
        for i in range(2, ceil(sqrt(N)) + 1):
            if not self.prime[i]: continue
            for j in range(i * i, N + 1, i):
                self.prime[j] = 0
        # adjs
        for v in range(1000, N):
            if not self.prime[v]: continue
            rs = (v % 1000, v // 1000 * 1000 + v % 100, v // 100 * 100 + v % 10, v // 10 * 10)
            for d in range(10):
                for nv in [d * m + r for r, m in zip(rs, (1000, 100, 10, 1))]:
                    if nv != v and nv > 1000 and self.prime[nv]:
                        self.adjs[v].add(nv)

    def shortestPath(self, Num1, Num2):
        if Num1 == Num2: return 0
        g = [10 ** 6] * 10000
        g[Num1] = 0
        q1, q2 = [], [Num1]
        dist = 1
        while q2:
            q1, q2 = q2, q1
            q2.clear()
            while q1:
                v = q1.pop()
                for nv in self.adjs[v]:
                    if dist < g[nv]:
                        if nv == Num2: return dist
                        g[nv] = dist
                        q2.append(nv)
            dist += 1
        return -1


# Driver code
if __name__ == '__main__':
    num1 = 1033
    num2 = 8179
    s = Solution()
    print(s.shortestPath(num1, num2))
