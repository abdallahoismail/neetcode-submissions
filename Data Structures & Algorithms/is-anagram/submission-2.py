class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return (Counter(s) == Counter(t))

# the order of chars does not matter
# the length of char matters
# len s == len t 