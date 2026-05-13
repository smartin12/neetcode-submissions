class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        subs = collections.defaultdict(set)
        for i, v in enumerate(nums):
            comp = target - v
            if v in subs.keys():
                return [subs[v], i]
            subs[comp] = i
