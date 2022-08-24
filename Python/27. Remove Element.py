class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)

        val = len(nums)

        return val