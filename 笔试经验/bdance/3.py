import heapq
def fun1(n0,m0,ai0,data0):
    # print(n0,m0,ai0,data0)
    ai0=list(sorted(ai0))
    data0=list(sorted(data0))
    lab=0
    ans=[0 for i in range(m0)]
    for i in range(m0):
        if i==0:
            while(lab<n0):
                if data0[i]>=ai0[lab]:
                    lab = lab + 1
                    ans[i]=lab
                else:
                    break
            # print(ans)
        else:
            lab=ans[i-1]
            ans[i]=ans[i-1]
            while (lab < n0):
                if data0[i] >= ai0[lab]:
                    lab = lab + 1
                    ans[i] = lab
                else:
                    break
    # print(ans)
    res=0
    for i in range(m0):
        if ans[i]>0:
            res=res+data0[i]-ai0[ans[i]-1]
        else:
            res=res+data0[i]
    print(res)








    # print(data0)




    pass

fun1(3,4,[50,100,200],[99,199,200,300])