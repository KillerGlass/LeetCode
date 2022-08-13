import numpy as np
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        aux = aux2 = aux1 = 0
        if( target !=0):
            for i, j in enumerate(nums):

                if target < 0:
                    aux1 = (j - target)
                    aux1*= -1
                    if (aux1 in nums and (target <= j or target == 0)):
                        if (j == aux1):
                            if (nums.count(j) > 1):
                                aux, aux2 = self.removeEqual(nums, i,j)
                            else:
                                continue
                        else:
                            aux, aux2 = i, nums.index(aux1)
                        break

                else:
                    aux1 = abs(j - target)

                    if( aux1 in nums and (target >= j or target == 0 )):
                        if( j == aux1 ):
                            if(nums.count(j) > 1):
                                aux, aux2 = self.removeEqual(nums, i, j)
                            else:
                                continue
                        else:
                            aux, aux2 = i, nums.index(aux1)
                        break
        else:
            if 0 in nums:
                aux, aux2 = self.removeEqual(nums, nums.index(0), 0)
            else:
                x = lambda x: x*-1 if x < 0 else x
                nums = list(map(x,nums))
                for i, j in enumerate(nums):
                    if(nums.count(j) > i):
                        aux, aux2 = self.removeEqual(nums, i, j)



        return [aux,aux2]

    def removeEqual(self,nums, i, j):
        nums.pop(i)
        return i, nums.index(j) + 1



test = Solution()
l = [-3,4,3,90]



print(test.twoSum(l,0))

