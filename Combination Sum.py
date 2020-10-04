class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        self.helper(candidates, 0, target,[], result)
        return result
    def helper(self, nums, next,target, partial, result):
        
        if target == 0:
            result.append(partial)
            return
        if next ==len(nums):
            return
        i = 0
        while target-i*nums[next] >=0:
            self.helper(nums, next+1, target-i*nums[next], partial + [nums[next]]*i, result)
            i += 1