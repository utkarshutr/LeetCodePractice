# User function Template for python3

class Solution:

    # Function to perform case-specific sorting of strings.
    def caseSort(self, s, n):
        lower_list = []
        upper_list = []
        ans = []

        for x in s:
            if x.islower():
                lower_list.append(x)
            else:
                upper_list.append(x)

        if lower_list:
            lower_list.sort()
        if upper_list:
            upper_list.sort()

        lower_index = 0
        upper_index = 0

        for i in range(s.__len__()):
            if s[i].islower():
                ans.append(lower_list[lower_index])
                lower_index += 1
            else:
                ans.append(upper_list[upper_index])
                upper_index += 1

        return "".join(ans)



if __name__ == '__main__':
    t = 1
    inputs_list = ["defRTSersUXI", "srbDKi"]
    for tt in inputs_list:
        n = int(tt.__len__())
        s = str(tt)
        print(Solution().caseSort(s, n))
