class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        string_map = {}
        for s in strs:
            letter_key = [0] * 26
            for letter in s:
                key = ord(letter) - 97
                letter_key[key] += 1
            key_hash = tuple(letter_key)
            if key_hash in string_map:
                string_map[key_hash].append(s)
            else:
                string_map[key_hash] = [s]
        return list(string_map.values())

        