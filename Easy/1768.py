class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)

        res = []
        for i in range(max(len1, len2)):
            if (i < len1):
                res.append(word1[i])
            if (i < len2):
                res.append(word2[i])
        return "".join(res)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.mergeAlternately("135", "24"))
    print(sol.mergeAlternately("rt", "trjhj"))
    print(sol.mergeAlternately("fghfghfgh", "jkk"))