"""
Solution Description:
 - This problem can be solved in 2 parts. In part 1, we can create a running sum array and
        in second part use this array to compare the sum of left and right parts.
 - Step 1:
    Iterate over each element. Put 0 at 0th position.
    Sum of current element is sum of sum till previous elements and current element.
        i.e sum[i] = sum[i] + num[i]

 - Step 2:
    Iterate for n times again.
        Left array sum = running sum of ith index (from step 1). We added 0 at 0th position,
            so we are getting sum till ith index at i position
        Right array sum = total sum (i.e. last element of running sum) - left array sum - current value nums list

    :return index element if left array sum and right array sum are equal
        otherwise - return -1
"""

from typing import List


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        running_sum_list = [0]
        for i in range(len(nums)):
            running_sum_list.append(nums[i] + running_sum_list[i])

        for i in range(len(nums)):
            left_array_sum = running_sum_list[i]
            right_array_sum = running_sum_list[-1] - left_array_sum - nums[i]

            if left_array_sum == right_array_sum:
                return i
        return -1


nums = [2, 3, -1, 8, 4]
# nums = [1, -1, 4]
# nums = [2, 5]
s = Solution()
print(s.findMiddleIndex(nums))
