class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.upper()
        s = s.strip()
        word = []
        i = 0
        j = 0
        while i in range(len(s)):
            if s[i].isalnum():
                word.append(s[i])
            i += 1
        while j in range(len(word) // 2):
            if word[j] == word[-j - 1]:
                j += 1
                continue
            else:
                return False
        return True
