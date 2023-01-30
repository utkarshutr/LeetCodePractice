class Solution:
    def dfs(self, graph, u, p):
        exc, inc = 0, 1
        for v in graph[u]:
            if v != p:
                cexc, cinc = self.dfs(graph, v, u)
                exc += cinc
                inc += min(cinc, cexc)
        return exc, inc

    def countVertex(self, N, edges):
        graph = [[] for _ in range(N)]
        for u, v in edges:
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)

        return min(self.dfs(graph, 0, -1))


if __name__ == '__main__':
    input1 = [6, 3]
    input2 = [["1 2", "1 3", "2 4", "3 5", "3 6"], ["1 2", "1 3"]]

    for in1, in2 in zip(input1, input2):
        edges = []
        for edge in in2:
            arr = list(map(int, edge.split()))
            edges.append(arr)

        ob = Solution()
        print(ob.countVertex(in1, edges))
