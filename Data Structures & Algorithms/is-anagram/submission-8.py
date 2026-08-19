class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        s_map = [0] * 26
        t_map = [0] * 26
        for sc, tc in zip(s.upper(), t.upper()):
            s_code = ord(sc) - 65
            print(s_code)
            s_map[s_code] += 1
            t_map[ord(tc) - 65] += 1
        return t_map == s_map
        