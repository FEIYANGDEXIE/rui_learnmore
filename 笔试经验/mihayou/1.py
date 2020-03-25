class Solution:
    def maxUncrossedLines(self , A , B ):
        # write code here
        # print(A)
        def fun1(s):
            if len(s)<2:
                return len(s)
            dp=[1 for i in s]
            n=len(s)
            temp=0
            for i in range(1,n):
                for j in range(i-1,-1,-1):
                    if s[i]>s[j]:

                        dp[i]=max(dp[i],dp[j]+1)
                    if temp<dp[i]:
                        temp=dp[i]
            # print(temp)
            return temp
        mat=[]
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i]==B[j]:
                    mat.append([i,j])
        # print(mat)
        arr=[]
        for i in mat:
            arr.append(i[1])
        return fun1(arr)






ress=Solution()
ress.maxUncrossedLines([2,5,1,2,5],[10,5,2,1,5,2])