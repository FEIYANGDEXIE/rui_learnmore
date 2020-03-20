st1=' a'
st2= 'a '
def fun1(s1,s2):
    s1=list(s1)
    s2=list(s2)
    i=0
    j=0
    ans=0
    while(i<len(s1) or j <len(s2)):
        print(i,j)
        if i<len(s1):
            if s1[i]==' ':
                i=i+1
                continue
        if j<len(s2):
            if s2[j]==' ':
                j=j+1
                continue
        if s1[i]!=' ' and s2[j]!=' ':
            if s1[i].lower()!=s2[j].lower():
                ans=1
            else:
                i=i+1
                j=j+1
    print(i,j)
    if i<len(s1) or j<len(s2):
        ans=1
    print(ans)
    return ans
res=fun1(st1,st2)
if res==0:
    print('yes')
else:
    print('no')



