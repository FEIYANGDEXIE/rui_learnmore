from itertools import combinations
class Solution:
    def solution(self , m , n ):
        ans=0
        for i in range(m,n+1):
            ans=ans+len(list(combinations([1,2,3,4,5,6,7,8,9],i)))
            print(i,len(list(combinations([1,2,3,4,5,6,7,8,9],i))))
        print(ans)
        return ans
a=Solution()
print(a.solution(1,2))