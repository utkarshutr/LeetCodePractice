# Declaring unordered map globally
map = {}


class Solution:
    def isScramble(self, S1: str, S2: str):
        # Strings of non-equal length can't be scramble strings
        if len(S1) != len(S2):
            return False

        n = len(S1)
        # Empty strings are scramble strings
        if not n:
            return True

        # Equal strings are scramble strings
        if S1 == S2:
            return True

        # Check for the condition of anagram - if strings are not anagram then those can't be scrambled
        if sorted(S1) != sorted(S2):
            return False

        # Checking if both Substrings are in map or are already calculated or not
        if S1 + ' ' + S2 in map:
            return map[S1 + ' ' + S2]

        # Declaring a flag variable
        flag = False

        for i in range(1, n):

            # Check
            # if S2[0...i] is a scrambled string of S1[0...i]
            # and
            # if S2[i+1...n] is a scrambled string of S1[i+1...n]
            if self.isScramble(S1[:i], S2[:i]) and self.isScramble(S1[i:], S2[i:]):
                flag = True
                return True

            # Check
            # if S2[0...i] is a scrambled string of S1[n-i...n]
            # and
            # S2[i+1...n] is a scramble string of S1[0...n-i-1]
            if self.isScramble(S1[-i:], S2[:i]) and self.isScramble(S1[:-i], S2[i:]):
                flag = True
                return True

        # Storing calculated value to map
        map[S1 + " " + S2] = flag

        return False


if __name__ == "__main__":
    input1 = ["coder ocred", "abcde caebd"]
    for input in input1:
        S1, S2 = input.split()
        if Solution().isScramble(S1, S2):
            print("Yes")
        else:
            print("No")
