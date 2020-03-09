import math
class Solution:
    def solution(self , n ):
        n2=int(math.sqrt(n*2))
        ans=0
        res=n
        for i in range(n2):
            ans=ans+(i+1)*(i+1)
            res=res-i-1
        ans=ans+res*(n2+1)

        print(ans)
        return ans
a=Solution()
a.solution(1)