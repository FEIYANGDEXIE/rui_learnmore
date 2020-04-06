data=[[0,30],[0,50],[10,20],[15,30],[20,50],[20,65]]
print(data)
def fun1(d):
    res=[]
    for i in range(len(d)):
        res.append([d[i][0],0])
        res.append([d[i][1], -1])

    res=list(sorted(res))
    # print(res)
    t=0
    ans=0
    for i in res:
        if i[1]==0:
            t=t+1
        else:
            t=t-1
        # print(t)
        ans=max(t,ans)
    # print(ans)
    return ans
fun1(data)

