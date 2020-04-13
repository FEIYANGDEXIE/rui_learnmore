import math
def fun1(num, data0):
    # print(num, data0)
    if num==1:
        print(0)
    else:
        i=num-1
        ans=0
        p=data0[i]
        i=i-1
        while(i>=0):
            if data0[i]<=p:
                p=data0[i]
                i=i-1
                continue
            else:
                if data0[i]%p==0:
                    sep = data0[i] // p
                    d = data0[i] // sep
                    p=d
                    ans = ans + sep - 1
                    i=i-1
                else:
                    sep=data0[i]//p+1
                    d=data0[i]//sep
                    r=data0[i]%sep
                    ans=ans+sep-1
                    p=d
                    i=i-1
        print(ans)













    pass
fun1(5,[3,5,13,9,12])