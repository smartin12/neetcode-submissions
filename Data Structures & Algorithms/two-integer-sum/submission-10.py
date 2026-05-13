class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        subs = {}
        for i, v in enumerate(nums):
            comp = target - v
            if comp in subs:
                return [subs[comp], i]
            subs[v] = i
