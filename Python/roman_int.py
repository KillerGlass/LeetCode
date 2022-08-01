class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman: str = s
        integer: int = 0

        integer += 1 * roman.count('I')
        integer += 5 * roman.count('V')
        integer += 50 * roman.count('L')
        integer += 100 * roman.count('C')
        integer += 500 * roman.count('D')
        integer += 10 * roman.count('X')
        integer += 1000 * roman.count('M')

        integer -= 2 * roman.count('IV')
        integer -= 2 * roman.count('IX')
        integer -= 20 * roman.count('XC')
        integer -= 20 * roman.count('XL')
        integer -= 200 * roman.count('CD')
        integer -= 200 * roman.count('CM')

        return integer

str = Solution()
print(str.romanToInt(input("digite : ")))
