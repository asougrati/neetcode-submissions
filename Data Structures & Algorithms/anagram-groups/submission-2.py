class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letter_map = {}
        for s in strs:
            letters = [0] * 26
            for c in s:
                if ord(c) > 96 and ord(c) < 123:
                    letters[ord(c) - 97] += 1
            key = tuple(letters)
            if key in letter_map:
                letter_map[key].append(s)
            else:
                letter_map[key] = [s]
        
        return list(letter_map.values())

        