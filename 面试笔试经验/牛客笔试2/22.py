def fun1(a):
    i=0
    ans=[]
    while(len(ans)<2 and i<10**5):
        pro=1
        for item in a:
            if item>i:
                tmp=i
            else:
                tmp = i % item
            pro=pro*tmp
        if pro !=0:
            ans.append(i)
            # print(i)
        # print(pro,i)
        i=i+1
    return ans
a=[2,3]
aa=fun1(a)
print(aa)