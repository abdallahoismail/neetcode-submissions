class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # if array has dups return true, no dups false
        return (len(nums) != len(set(nums)))