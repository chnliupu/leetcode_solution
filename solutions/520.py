class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        def isUpper(char: str):
            if ord(char) < ord('A') or ord(char) > ord('Z'):
                return False
            return True
        prevIsUpper = word[0].isupper()
        for i in range(1, len(word)):
            currentIsUpper = word[i].isupper()
            if currentIsUpper and not prevIsUpper:
                return False
            elif not currentIsUpper and prevIsUpper and i != 1:
                return False
            prevIsUpper = currentIsUpper
        return True

sol = Solution()
print(sol.detectCapitalUse("USA"))
print(sol.detectCapitalUse("FlaG"))
print(sol.detectCapitalUse("aabb"))
print(sol.detectCapitalUse("aabB"))

                