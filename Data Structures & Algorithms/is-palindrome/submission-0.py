class Solution:
    def isPalindrome(self, s: str) -> bool:
        fwd = 0
        rev = len(s) - 1
        for i in range(len(s)):
            front = s[fwd].lower()
            back = s[rev].lower()
            print(f"Pointer1: {front}, Pointer2: {back}")
            if not front.isalnum():
                fwd += 1
                continue
            if not back.isalnum():
                rev -= 1
                continue
            if not front == back:
                return False
            fwd += 1
            rev -= 1
        return True