class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s, count_t = Counter(s), Counter(t)
        return (True if count_s == count_t else False)
