class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {} # map v to idx
        for idx, num in enumerate(nums):
            complement = target - num # 7-3=4 (1st iter)
            if complement in num_map: # is 4 in map -> no -> add it and its idx
                return [num_map[complement], idx]
            # else add the element to the map
            num_map[num] = idx # {3:0}


# nums = [3,4,5,6]
#        [0,1,2,3]
# target = 7 



