class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        lis = accounts
        maior =  max([sum(i) for i in lis])
        return maior

test = Solution()
test.maximumWealth([[1,5],[7,3],[3,5]])
