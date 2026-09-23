class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous_map = {} # add visited elements

        for i, num in enumerate(nums):
            previous_map[num] = i

        for i, num in enumerate(nums):
            diff = target - num
            if diff in previous_map and previous_map[diff] != i:
                return [i, previous_map[diff]]
        return []
