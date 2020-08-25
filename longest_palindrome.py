class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        letters = set()
        for c in s:
            if c in letters:
                max_length += 2
                letters.remove(c)
            else:
                letters.add(c)
        return max_length +bool(letters)