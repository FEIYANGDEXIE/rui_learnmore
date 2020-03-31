data = [1, 2, 1,0,1]
n = 5

def backtrack(num, a,b):
    if num==n:
        # print(a)
        lab[0]=lab[0]+a
        lab[1]=lab[1]+1
    else:
        if data[num]==2:
            b1=b+1
            a1=a+b1
            backtrack(num+1,a1,b1)
            b2=0
            backtrack(num+1,a,b2)
        elif data[num]==1:
            b=b+1
            a=a+b
            backtrack(num+1,a,b)
        else:
            b=0
            backtrack(num+1,a,b)

lab = [0, 0]
backtrack(0,0,0)
print(lab[0]//lab[1])

