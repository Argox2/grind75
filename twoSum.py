from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_idx = {}

        for idx, num in enumerate(nums):
            complement = target - num

            if complement in num_to_idx:
                return [num_to_idx[complement], idx]

            num_to_idx[num] = idx
