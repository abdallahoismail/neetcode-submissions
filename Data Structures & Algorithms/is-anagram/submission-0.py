class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # brute force
        return sorted(s) == sorted(t)
# TC of sorting is O(n logn)
# we sort 2 different strings
# overall TC is O(n logn) + O(m logm), where n, m are the lengths of s, t respectively

        