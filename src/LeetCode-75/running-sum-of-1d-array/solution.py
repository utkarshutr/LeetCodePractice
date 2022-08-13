"""
Solution Description:
 - Idea is to have an addition result array running_sum_list.
 - Iterate over each element. Sum of current element would be sum of sum till previous elements and current element.
        i.e sum[i] = sum[i-1] + num[i]
"""

from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum_list = []
        for i in range(len(nums)):
            running_sum_list.append(nums[i] + (0 if i == 0 else running_sum_list[i - 1]))

        return running_sum_list


nums = [1, 2, 3, 4]
s = Solution()
print(s.runningSum(nums))
