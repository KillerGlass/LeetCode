class Solution:
    def firstUniqChar(self, s: str) -> int:

        string = set(s)
        ind = -1
        for i in s:
            if s.count(i) == 1:
                ind = s.index(i)
                break

        return ind


test = Solution()
s = "loveleetcode"
print(test.firstUniqChar(s))
