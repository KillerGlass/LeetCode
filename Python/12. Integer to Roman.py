

class Solution:

    def intToRoman(self, num: int) -> str:
        """
        :type s: str
        :rtype: int
        """
        self.s = ''
        num = self.integerMDC(num,1000, "M")
        num = self.intengerDLV(num, "00", ("CM","D","CD"))

        num = self.integerMDC(num, 100, "C")
        num = self.intengerDLV(num, "0", ("XC", "L", "XL"))

        num = self.integerMDC(num, 10, "X")
        num = self.intengerDLV(num, '', ("IX", "V", "IV"))

        num = self.integerMDC(num, 1, "I")

        return self.s


    def integerMDC(self,num, div, carac):

        flag = int(num / div)
        if (flag):
            self.s += flag * carac
            num = num % div

        return num

    def intengerDLV(self,num,zeros,charc):

        if num >= int('9' + zeros):
            self.s += charc[0]
            num = num%int('9' + zeros)
        elif num >= int('5' + zeros):
            self.s += charc[1]
            num = num % int('5' + zeros)
        elif num >= int('4' + zeros):
            self.s += charc[2]
            num = num % int('4' + zeros)

        return num