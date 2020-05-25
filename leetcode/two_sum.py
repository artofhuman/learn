from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        hash_map = {}
        for i in range(size):
            complement = target - nums[i]
            if complement in hash_map:
                return [hash_map[complement], i]
            hash_map[nums[i]] = i


assert Solution().twoSum([2, 7, 11, 55], 9) == [0, 1]
assert Solution().twoSum([3, 3], 6) == [0, 1]
