class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        target = -1

        if needle in haystack:
            target = haystack.index(needle)


        return target



test = Solution()
l =  "aaaaa"
print(test.strStr(l, "bba"))