class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_list = list(t)
        if len(s) != len(t):
            return False
        for char in s:
            if not char in t_list:
                return False
            t_list.remove(char)
        return True