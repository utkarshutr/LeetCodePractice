class Solution:
    def endPoints(self, matrix, R, C):
        i, j = 0, 0
        direction = 1  # right =1, down=2, left = 3, up = 4
        while 1:
            if matrix[i][j] == 1:
                matrix[i][j] = 0
                direction += 1
                if direction == 5:
                    direction = 1

            last_location = [i, j]
            if direction == 1:
                j += 1
            elif direction == 2:
                i += 1
            elif direction == 3:
                j -= 1
            else:
                i -= 1

            if i < 0 or j < 0 or i >= R or j >= C:
                break

        return last_location


if __name__ == '__main__':
    input1 = ["2 2", "3 5", "10 10"]
    input2 = [["0 1", "1 0"], ["0 1 1 1 0", "1 0 1 0 1", "1 1 1 0 0"],
              ["0 1 1 0 0 1 1 1 1 0", "1 0 1 0 0 1 0 0 1 0", "0 0 1 1 0 0 0 0 0 1", "1 0 0 0 0 1 1 1 0 0", "1 1 1 0 0 1 0 0 0 1", "0 0 1 1 0 1 1 0 1 1", "1 1 1 0 1 0 1 1 1 1", "1 1 0 0 1 0 0 1 0 0", "0 0 0 1 1 0 1 0 0 0", "1 0 1 1 0 1 1 1 0 0"]]
    for in1, in2 in zip(input1, input2):
        r, c = map(int, in1.strip().split())
        matrix = []
        for i in range(r):
            line = [int(x) for x in in2[i].strip().split()]
            matrix.append(line)
        ob = Solution()
        ans = ob.endPoints(matrix, r, c)
        print('(', ans[0], ', ', ans[1], ')', sep='')
