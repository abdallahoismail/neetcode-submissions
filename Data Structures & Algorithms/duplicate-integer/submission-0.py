class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted_list = sorted(nums)
        for i in range(len(sorted_list) - 1):
            if sorted_list[i] == sorted_list[i+1]:
                return True
        return False

# time complexity for sorting is O(n logn)
# time complexity for loop is O(n)
# the operation with higher order time complexity dominates
# so sorting is the slower op
# overall TC of solution is O(n logn)

# space complexity: we create a new list that has n element so O(n)
# the loop uses a few vars so the SC is O(1)

# notes on solution 
'''
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted_list = sorted(nums, reverse=True)
        for i in range(len(sorted_list)):
            if sorted_list[i] == sorted_list[i+1]:
                return True
            else:
                return False
'''
# X the program returns T/F prematurely as it checks the first 2 elements
# the way the loop is setup, will run into an index out of bounds error because when we get to the end of the list at idx i, we check for element at i+1 (which does not exist)
