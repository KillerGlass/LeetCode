class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        ord = { i: len(i) for i in strs}
        ord = sorted(ord.items(), key=lambda item: item[1])
        world= ord[0][0] + 'p'
        cont = 0
        prefix = ""
        #print(world)
        for i in range(1,len(world)):
            i *= -1
            for j in strs:
                j +=   'p'
                j = j[ :  (len(world) )]

                #print(world[:i], j, world[:i ] in j[:i] )

                if world[:i] in j[:i]:
                    cont +=1
                else:
                    break

            if(cont == len(strs)):
                prefix =  world[:i]
                break
            cont = 0

        return prefix



test = Solution()
l =["a"]
print(test.longestCommonPrefix(l))