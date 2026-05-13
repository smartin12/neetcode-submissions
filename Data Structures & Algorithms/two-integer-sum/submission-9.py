class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        subs = {}
        for i, v in enumerate(nums):
            comp = target - v
            if v in subs:
                return [subs[v], i]
            subs[comp] = i
