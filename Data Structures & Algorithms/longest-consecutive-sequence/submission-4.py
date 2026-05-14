class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 1:
                return 1
        max_run = 0
        current_run = 1
        c = 1
        p = 0
        loop_count = 0
        nums.sort()
        while c < len(nums):
            loop_count += 1
            if nums[c] == nums[p] + 1:
                current_run += 1
            elif nums[c] != nums[p] + 1 and nums[c] != nums[p]:
                current_run = 1
            c += 1
            p += 1
            if current_run > max_run:
                    max_run = current_run
        return max_run
