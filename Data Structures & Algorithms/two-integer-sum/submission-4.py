class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {} # map v to idx
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], idx]
            # else add the element to the map
            num_map[num] = idx


# nums = [3,4,5,6]
#        [0,1,2,3]
# target = 7 



