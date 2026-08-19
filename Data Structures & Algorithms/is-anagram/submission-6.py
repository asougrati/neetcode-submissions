class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        s_map = defaultdict(int)
        t_map = defaultdict(int)
        for s_char, t_char in zip(s, t):
            s_map[s_char] += 1
            t_map[t_char] += 1
        return t_map == s_map
        