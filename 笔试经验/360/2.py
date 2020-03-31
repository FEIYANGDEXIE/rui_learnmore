n=4
def backtrack(num,assign):
    if len(assign)==2:
        # print(assign,num)
        tmp=[assign[0],assign[1],num]
        tmp=tuple(sorted((tmp)))
        if tmp not in d:
            d[tmp]=0

            s1=(assign[0]+2)*(assign[1]+2)*(num+1)
            s2 = (assign[0] + 2) * (assign[1] + 1) * (num + 2)
            s3 = (assign[0] + 1) * (assign[1] + 2) * (num + 2)

            lab[0]=max(lab[0],max(s1,s2,s3))
    else:
        for i in range(1,num+1):
            if num%i==0:
                l_a=assign.copy()
                l_a.append(i)
                backtrack(num//i,l_a)
    pass

d={}
lab=[0]

backtrack(n,[])
print(lab[0]-n)













