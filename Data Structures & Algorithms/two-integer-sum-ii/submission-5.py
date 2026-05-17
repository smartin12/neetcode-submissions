class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while r > l:
            if numbers[r] + numbers[l] == target:
                return [l + 1, r + 1]
            elif numbers[r] + numbers[l] >= target:
                print(f'R, {r} is greater than {target}.')
                r -= 1
                print(f'R is now {r}.')
            elif numbers[l] + numbers[r] > target:
                print(f'R, {r} + L, {l} is MORE than {target}.')
                r -= 1
                print(f'R is now {r}.')
            else:
                print(f'R, {r} + L, {l} is LESS than {target}.')
                l += 1
                print(f'L is now {l}.')

