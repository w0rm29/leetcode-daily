"""
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

Example:
    Input: nums = [1,2,3,1,1,3]
    Output: 4
    Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
"""

##########################
# Solution 1
##########################

from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(0, len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
        return count
    
########################
# Solution 2
########################

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic = {}
        count = 0

        for num in nums:
            if num not in dic:
                dic[num] = 0
            else:
                dic[num] += 1
                count += dic[num]
        return count