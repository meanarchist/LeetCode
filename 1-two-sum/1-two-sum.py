class Solution(object):
    def twoSum(self, nums, target):
        dic={}
        for i, v in enumerate(nums):
            remaining = target - v
            if remaining in dic:
                return [dic[remaining], i]
            dic[v] = i
        return []