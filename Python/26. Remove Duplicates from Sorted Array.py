class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        aux1 = list(set(nums))
        nums.clear()
        aux1.sort()
        nums += aux1

        return len(nums)






test = Solution()
nums = [-1,0,0,0,0,3,3]
k = test.removeDuplicates(nums)#Calls your implementation

expectedNums = [-1,0,3]
print(nums)
k1 = len(expectedNums)
for i in range(0,k):
    print( nums[i] == expectedNums[i])
