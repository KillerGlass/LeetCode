class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:

        return [sum(nums[:i ]) + j for i, j in enumerate(nums)]



test = Solution()
print(test.runningSum([1,2,3,4]))



