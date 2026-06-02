class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        max_s = len(strs)
        for s, st in enumerate(strs):
            if s < max_s:
                encoded += f'{len(st)}#' + st

        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        
        while i < len(s):
            # Find the position of the next delimiter
            j = i
            while s[j] != '#':
                j += 1
            
            # Extract the length and the string
            length = int(s[i:j])
            i = j + 1
            being_parsed = s[i : i + length]
            result.append(being_parsed)
            
            # Move pointer to the start of the next length
            i += length

        return result