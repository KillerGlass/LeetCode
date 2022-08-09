class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = list(dict.fromkeys(ransomNote))

        b = magazine
        flag = True
        for i in a:
            print(ransomNote.count(i) , b.count(i))
            if(ransomNote.count(i) > b.count(i)):
                flag = False
                break

        return flag



test = Solution()
print(test.canConstruct("aa","ab"))