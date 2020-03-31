data=[1,2,1]
n=3


def backtrack(num,assign):
    if num==n:
        # print(assign)
        s=0
        ans=0
        for  i in assign:
            if i==1:
                s=s+1
                ans=ans+s
            else:
                s=0
        lab[0]=lab[0]+ans
        lab[1]=lab[1]+1
    else:
        if data[num]==2:
            l_a=assign.copy()
            l_a.append(0)
            backtrack(num+1,l_a)
            l_b = assign.copy()
            l_b.append(1)
            backtrack(num + 1, l_b)
        else:

            l_a=assign.copy()
            l_a.append(data[num])
            backtrack(num+1,l_a)

lab=[0,0]
backtrack(0,[])
backtrack2
print(lab[0]//lab[1])