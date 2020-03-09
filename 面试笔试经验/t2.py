class Solution:
    def solution(self, n):
        f=[2,3,4,5,6,7,8,9]
        res=''
        while(n>9):
            old=n
            for i in range(7,-1,-1):
                if n%f[i]==0:
                    n=n//f[i]
                    print(n)
                    res=res+str(f[i])
                    break
            if n==old:
                return -1
        if n>9:
            return -1
        else:
            res=res+str(int(n))
        return res[::-1]


        # print(idx)
a=Solution()
print(a.solution(56))
