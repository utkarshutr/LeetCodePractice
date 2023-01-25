"""
Solution Description:
 - If you thought of very basic solution.py to check number of unique characters in each string. You are 50% correct.
    But some test cases may fail. For example: s=abab, t=bbbb -- these are not isomorphic

 - So, the first step is to check number of unique characters. If unique characters don't match, means not isomorphic.
 - Next, we will maintain a dictionary of mapping. Iterate over each character of both strings:
        - If both characters are not in the dictionary - put them left string character as key and right as value
        - If any of character is in mapping dictionary, check for mapping is correct or not.
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict_mapping = {}
        if len(set(s)) == len(set(t)):
            for s_char, t_char in zip(s, t):
                print(s_char, t_char)
                if s_char not in dict_mapping.keys() and t_char not in dict_mapping.values():
                    dict_mapping[s_char] = t_char
                elif dict_mapping[s_char] != t_char:
                    return False
            return True
        else:
            return False


s = "bbbaaaba"
t = "aaabbbba"
sol = Solution()
print(sol.isIsomorphic(s, t))
