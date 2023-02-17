from collections import deque


class Solution():

    def bfs(self, mat, n, m, src):
        Q = deque(src)
        visited = set(src)
        while Q:
            x, y = Q.popleft()
            for nx, ny in [[x, y + 1], [x, y - 1], [x + 1, y], [x - 1, y]]:
                if 0 <= nx < n and 0 <= ny < m and mat[nx][ny] >= mat[x][y] and (nx, ny) not in visited:
                    Q.append((nx, ny))
                    visited.add((nx, ny))
        return visited

    def water_flow(self, mat, n, m):
        # Perform BFS/DFS from cells on top and left edge. (Visting the neighbours with height equal or higher)
        visited1 = self.bfs(mat, n, m, [(i, 0) for i in range(n)] + [(0, j) for j in range(m)])

        # Perform BFS/DFS from cells on bottom and right edge. (Visting the neighbours with height equal or higher)
        visited2 = self.bfs(mat, n, m, [(i, m - 1) for i in range(n)] + [(n - 1, j) for j in range(m)])

        # Return count of the cells which are visited both
        return len(visited1 & visited2)


if __name__ == "__main__":
    input1 = ["5 5"]
    input2 = [["1 3 3 2 4", "4 5 6 4 4", "2 4 5 3 1", "6 7 1 4 5", "6 1 1 3 4"]]
    for in1, in2 in zip(input1, input2):
        n, m = map(int, in1.split())
        mat = []
        for row in in2:
            tmp = [int(i) for i in row.split()]
            mat.append(tmp)
        print(Solution().water_flow(mat, n, m))
