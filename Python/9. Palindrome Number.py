class Solution:
    def isPalindrome(self, x: int) -> bool:

        a = str(x)
        return a == a[::-1]


test = Solution()
print(test.isPalindrome(122))
