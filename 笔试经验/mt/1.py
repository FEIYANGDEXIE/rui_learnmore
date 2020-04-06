n=5
x=2
data=[1,2,5,7]
data=list(sorted(data))
def bt(x0,x1):
    try:
        return d[(x0,x1)]
    except:

        if data[x1]-data[x0]<=x:
            d[(x0,x1)]=0
            return 0
        elif x1==x0:
            d[(x0,x1)]=0
            return 0
        else:
            d[(x0,x1)]=min(bt(x0+1,x1),bt(x0,x1-1))+1
            return min(bt(x0+1,x1),bt(x0,x1-1))+1
d={}

ans=bt(0,len(data)-1)
print(ans)