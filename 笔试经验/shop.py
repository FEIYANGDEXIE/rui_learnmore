
def backtrack(assign):
    if len(assign)==len(a):
        # print(assign)
        tmp=list(map(str,assign))
        tmp=int(''.join(tmp))
        ans[0]=max(ans[0],tmp)

    else:
        for i in range(len(a)):
            if a[i] not in assign:
                l_a=assign.copy()
                l_a.append(a[i])

                backtrack(l_a)
def fun2(s):
    #还是错的
    r=max(s)//10
    b=[0 for i in range(len(s))]
    for i in range(len(s)):
        tmp=list(str(s[i]))
        tmp=list(map(int,tmp))
        if len(tmp)<r:
            b[i]=r-len(tmp)
            for j in range(r-len(tmp)):
                tmp.append(0)


        s[i]=[tmp,b[i]]
    print(b)
    s=list(sorted(s,reverse=True))
    print(s)
    for i in range(len(s)):
        s[i]=s[i][0][0:len(s[i][0])-s[i][1]]
    print(s)



    pass

a = [30, 3, 34, 5, 9]
b=[0 for i in range(len(a))]
ans=[0]
backtrack([])
print(ans[0])
fun2(a)