import heapq


def fun1(n0, m0, ai0, data0):
    ans=[]
    for i in ai0:
        ans.append([i,0])
    for i in data0:
        ans.append([i,1])
    ans=list(sorted(ans,key=lambda x:x[0]))
    # print(ans)
    lab=0
    res=0
    for i in ans:
        if i[1]==0:
            lab=i[0]
        else:
            res=res+i[0]-lab
    print(res)

    # print(n0,m0,ai0,data0)




fun1(3, 4, [50, 100, 200], [99, 199, 200, 300])