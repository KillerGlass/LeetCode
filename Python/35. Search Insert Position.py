class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:


        if target in nums:
            ind = nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            ind =  nums.index(target)

        return ind


test = Solution()
l = [1,3,5,6]
print(test.searchInsert(l,7))
