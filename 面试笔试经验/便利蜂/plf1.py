a='3,6,5,1,8'
#

def backtrack(a,b):
    if str(a) + '-' + str(b) in d:
        return d[str(a) + '-' + str(b)]
    # print(a,b)
    if sum(data[a:b+1])%3==0:
        d[str(a)+'-'+str(b)]=sum(data[a:b+1])//3
        return sum(data[a:b+1])//3
    else:
        if a==b:
            d[str(a) + '-' + str(b)] = sum(data[a:b + 1]) // 3
            return 0
        else:
            tmp=0
            for i in range(a,b):
                lab=backtrack(a,i)+backtrack(i+1,b)
                # print(lab)
                tmp=max(lab,tmp)
            d[str(a) + '-' + str(b)] = tmp
            return tmp
a=a.split(',')
a=list(map(int,a))
# print(a)
ans=0
data=[]
for i in a:
    if i%3==0:
        ans=ans+i//3
    else:
        data.append(i)
# print(data)
d={}
res=backtrack(0,len(data)-1)
print(res+ans)



