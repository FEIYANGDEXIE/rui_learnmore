n=3
p=[0.90,0.10,0.10]
a=[2,1,1]
#
sc=[]
for i in range(n):
    sc.append(p[i]*a[i])
# print(sc)
def bt(num,assign,pp):
    if num==0:
        # print(pp)
        res[0]=max(res[0],pp)
    for i in range(n):

        if i+1<=num:
            l_a=assign.copy()
            ans=sc[i]
            for j in assign:
                ans=ans*j
            pp=pp+ans
            l_a.append(p[i])
            bt(num-i-1,l_a,pp)
res=[0]
bt(n,[],0)
print(res[0])
