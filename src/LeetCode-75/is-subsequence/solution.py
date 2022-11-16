"""
Solution Description:
 - First we need to check which string will be the subsequence.
    The smaller string can be subsequence and we will check with other string.
    We are calling the subsequence string as first string and other one as second string.
 - Once we have both the strings, start iteration from o index for both strings.
    - if both characters are matching, then increment both
    - if not matched, increment the second string - we are treating this char as deleted character.
    - we will end the loop when iteration of any strings completed.

    returns:
    True: if first string iteration completed - it is sequence. We found all characters in sequence in second string.
    False: else - means first string iteration not completed, all characters not foung in sequence.
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_len, t_len = len(s), len(t)
        if s_len == 0 and t_len == 0:
            return True
        if s_len == 0 and t_len > 0:
            return True
        if s_len > 0 and t_len == 0:
            return False

        if s_len > t_len:
            first_str, second_str = t, s
        else:
            first_str, second_str = s, t

        index_first_str, index_second_str = 0, 0
        while index_first_str < len(first_str) and index_second_str < len(second_str):
            if first_str[index_first_str] == second_str[index_second_str]:
                index_first_str += 1
                index_second_str += 1
            else:
                index_second_str += 1

        if index_first_str == len(first_str):
            return True
        else:
            return False


s = "axc"
t = "adhxhc"
sol = Solution()
print(sol.isSubsequence(s, t))
