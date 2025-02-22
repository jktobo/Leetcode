class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        sl = list(s)
        l = 0
        r = len(s) - 1
        while (l < r):
            while (l < r and s[l] not in vowels):
                l += 1
            while (l < r and s[r] not in vowels):
                r -= 1
            sl[l], sl[r] = sl[r], sl[l]
            l += 1
            r -= 1
        return "".join(sl)  