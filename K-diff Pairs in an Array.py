from collections import Counter
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        
        freq = Counter(nums)
        pairs = 0
        
        for num in freq:
            if k == 0:
                if freq[num] > 1:
                    pairs += 1
            else:
                if num + k in freq:
                    pairs += 1
        return pairs
            
        