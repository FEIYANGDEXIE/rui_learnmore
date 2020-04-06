import copy
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        def bt(s,assign):

            if len(s)==0:
                # print(assign)
                if ans[0]!='x':
                    ans[0]=min(ans[0],int(assign))
                else:
                    ans[0]=int(assign)
            else:
                for  i in range(len(s)):
                    l_s=copy.copy(s)
                    del l_s[i]
                    l_a=assign+str(s[i])
                    bt(l_s,l_a)
        ans=['x']
        bt(numbers,'')

        return ans[0]
a=Solution()
print(a.PrintMinNumber([3,32,321]))

