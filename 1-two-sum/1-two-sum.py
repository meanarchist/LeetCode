class Solution(object):
    def twoSum(self, nums, target):
        dic={}
        for i, v in enumerate(nums):
            r= target - v
            if r in dic:
                return [dic[r], i]
            dic[v] = i
        return []