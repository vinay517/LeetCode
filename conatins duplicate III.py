class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k<=0 or t < 0:
            return False
        buckets = {}
        for i, num in enumerate(nums):
            bucket = num // (t+1)
            if bucket in buckets:
                return True
            if bucket+1 in buckets and abs(num - buckets[bucket + 1]) <= t:
                return True
            if bucket-1 in buckets and abs(num - buckets[bucket - 1]) <= t:
                return True
            buckets[bucket] = num
            if i-k >= 0:
                old_bucket = nums[i-k] //(t+1)
                del buckets[old_bucket]
                
        return False