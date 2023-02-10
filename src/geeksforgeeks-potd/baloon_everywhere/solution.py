class Solution:
    def maxInstance(self, s: str) -> int:
        baloon_dict = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}
        for c in s:
            if c in baloon_dict:
                baloon_dict[c] += 1

        char_counts = baloon_dict.values()
        min_val = min(char_counts)
        o_count = baloon_dict["o"]
        l_count = baloon_dict["l"]
        return min(min_val, o_count // 2, l_count // 2)


if __name__ == "__main__":
    input1 = ["nlaebolko", "loonbalxballpoon", "bnlbllanmbaamnmobbanablboolonlol"]
    for in1 in input1:
        s = in1

        obj = Solution()
        res = obj.maxInstance(s)

        print(res)
