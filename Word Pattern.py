class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split()
        if len(str) != len(pattern):
            return False
        
        p_to_s, s_to_p = {}, {}
        for w, c in zip(str, pattern):
            
            if c in p_to_s and p_to_s[c] != w:
                return False
            p_to_s[c] = w
            
            if w in s_to_p and s_to_p[w] != c:
                return False
            s_to_p[w] = c
        return True