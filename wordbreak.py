class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        can_make = [False] * (len(s)+1)
        can_make[0] = True
        
        for i in range(1, len(s)+1):
            for j in range(i-1, -1, -1):
                if can_make[j] and s[j:i] in wordDict:
                    can_make[i] = True
                    break
        return can_make[-1]