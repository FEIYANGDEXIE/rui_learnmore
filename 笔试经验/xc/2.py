n1=5
m1=5
p1=[2,4]
x1=5
def fun1(n,m,p,x):
    q=[]
    d={}
    for i in p:
        d[i]=0
    q.append([n,m])
    while(q):
        x=x-1
        if x==0:
            break
        p=[]
        while(q):
            tmp=q.pop(0)
            if tmp[1]-1>0:
                p.append([tmp[0],tmp[1]-1])

            key1=n-tmp[1]+1
            if key1 in d:
                p.append([n,m])
        print(p)
        q=p
    print(len(q)*n)
fun1(n1,m1,p1,x1)