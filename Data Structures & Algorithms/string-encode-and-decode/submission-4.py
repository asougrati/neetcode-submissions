class Solution:

    def encode(self, strs: List[str]) -> str:
        string_list = []
        if len(strs) == 0:
            # print("")
            return ""
        for s in strs:
            length = len(s)
            encoded_part = f"{length}#{s}#"
            string_list.append(encoded_part)
        encoded_string = "".join(string_list)
        # print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        result = []
        if len(s) == 0:
            return result
        length = None
        chars = None
        for c in s:
            # print (f"Length:{length}")
            # print(f"Chars:{chars}\n")
            if not chars == None:
                if length == 0:
                    length = None
                    string = "".join(chars)
                    result.append(string)
                    chars = None
                    continue
                else:
                    chars.append(c)
                    length -= 1
                    continue
            if length == None:
                length = int(c)
                continue
            if chars == None:
                if c == '#':
                    chars = []
                    continue
                elif length:
                    length *= 10
                    length += int(c)
                    continue       
        return result
