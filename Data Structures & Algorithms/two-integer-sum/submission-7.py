class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_hmap = {}
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in num_hmap:
                return [num_hmap[diff], i]
            num_hmap[num] = i