class Solution:
    def minRemove(self , s ):
        l_u=[]
        l={}
        r={}
        for i in range(len(s)):
            if s[i]=='(':
                l_u.append(i)
                l[i]=1
            elif s[i]==')':
                if len(l_u)<=0:
                    r[i]=1
                else:
                    idx=l_u.pop()
                    del l[idx]
        res=''
        d={}

        for i in l:
            d[i]=1

        for j in r:
            d[j]=1
        # print(l,r,d)
        for i in range(len(s)):
            try:
                d[i]=d[i]+1
            except:
                res=res+s[i]
        # print(res,'ss')
        return res

ss=Solution()
ss.minRemove("))((")
