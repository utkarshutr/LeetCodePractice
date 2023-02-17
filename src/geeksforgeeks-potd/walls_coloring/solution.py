"""
Approach:
    Approach is simple, we will iterate over all the colors, total cost till now will be addition of current cost
    and minimum of total cost of other 2 colors calculated till now
"""


class Solution():
    def minCost(self, colors, N):
        pink_cost, black_cost, yellow_cost = 0, 0, 0

        for color_list in colors:
            net_pink_cost = color_list[0] + min(black_cost, yellow_cost)
            net_black_cost = color_list[1] + min(pink_cost, yellow_cost)
            net_yellow_cost = color_list[2] + min(pink_cost, black_cost)
            pink_cost, black_cost, yellow_cost = net_pink_cost, net_black_cost, net_yellow_cost

        return min(pink_cost, black_cost, yellow_cost)


if __name__ == "__main__":
    input_count = ["3", "2"]
    input_colors = [["14 2 11", "11 14 5", "14 3 10"], ["1 2 3", "1 4 6"]]
    for in_cnt, in_colors in zip(input_count, input_colors):
        n = int(in_cnt)
        colors = []

        for i in range(n):
            tmp = [int(x) for x in in_colors[i].split()]
            colors.append(tmp)

        print(Solution().minCost(colors, n))
