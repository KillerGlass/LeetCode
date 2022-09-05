def search(j):

    if j == '(':
        carc =  ')'
    elif j == '{':
        carc =  '}'
    elif j == '[':
        carc =  ']'

    return  carc

class Solution:
    def isValid(self, s: str) -> bool:

        valid = True
        cont = 0
        s = list(s)
        lis = []
        for i,j in enumerate(s):

            if j == '(' or j == '{' or j == '[':
                lis.insert(0,search(j))
                cont +=1

            elif j == ')' or j == '}' or j == ']':
                if lis != [] and lis[0]== j:
                    lis.pop(0)

                else:
                    valid = False
                    break



        if cont == 0 or len(s) / cont != 2:
            valid = False


        return valid


test = Solution()
nums = ")(){}"
print(test.isValid(nums))