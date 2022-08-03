class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        number = num
        cont = 0
        while(number):
            cont +=1

            if(number % 2 == 0):
                number /= 2
            else:
                number -=1


        return cont

test = Solution()
print(test.numberOfSteps(14))