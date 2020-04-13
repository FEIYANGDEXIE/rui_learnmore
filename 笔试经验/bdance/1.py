def fun1(d1,d2,num):
    # print(d1,d2)
    ans=0
    for i in range(num):
        d1[i]=d1[i]-d2[i]
    # print(d1)
    lab=0
    res=0
    for i in range(num):
        # print(d1[i],ans,lab)
        if lab==0 and d1[i]==0:
            continue
        elif lab==0 and d1[i]!=0:
            lab=1
            res=d1[i]
        elif lab==1 and d1[i]==res:
            continue
        elif lab==1 and d1[i]!=res:
            if d1[i]==0:
                lab=2
                continue
            else:
                ans=1
        elif lab==2 and d1[i]==0:
            continue
        else:
            ans=1
    # print(ans)
    if ans==0:
        print('YES')
    else:
        print('NO')







    pass

fun1([3,7,1,4,1,2],[3,7,3,6,3,2],6)
fun1([1,1,1,1,1],[1,2,1,3,1],5)