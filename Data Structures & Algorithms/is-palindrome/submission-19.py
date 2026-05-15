class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        s = s.lower()
        while r > l:
            print(f'l: {l}\ns[l]: {s[l]}\nr: {r}\ns[r]: {s[r]}')
            if s[l] != s[r]:
                if s[l].isalnum() and s[r].isalnum():
                    return False
                if not s[r].isalpha():
                    r -= 1
                    continue
                if not s[l].isalpha():
                    l += 1
                    continue
            else:
                l += 1
                r -= 1
        return True
            