class Solution:
    @lru_cache(maxsize=None)
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) == 1:
            return (s1 == s2)
        if sorted(s1) != sorted(s2):
            return False
        else:
            for k in range(1, len(s1)):
                if (self.isScramble(s1[:k], s2[:k]) and self.isScramble(s1[k:], s2[k:])) or (self.isScramble(s1[:k], s2[-k:]) and self.isScramble(s1[k:], s2[:-k])):
                    return True
            return False