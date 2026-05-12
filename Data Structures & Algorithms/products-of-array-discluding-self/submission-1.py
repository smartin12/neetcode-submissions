class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        z_count = 0
        for i in nums:
            if i != 0:
                total *= i
            else:
                z_count += 1
                if z_count > 1:
                    return [0 for i in nums]
        if z_count == 1:
            res = [0 if i != 0 else total for i in nums]
        else:
            res = [int(total / i) for i in nums]
        return res      

            

