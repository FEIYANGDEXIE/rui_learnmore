a='[1,2],[2,3],[3,4],[4,5],[5,3]'
#使用一维数组存储单链表
a=a.split(',')
# print(a)
ans=[]
for i in a:
    tmp=''
    for j in i:
        if j.isdigit():
            tmp=tmp+j
    ans.append(int(tmp))
print(ans)
res=ans[1:len(ans):2]
print(res)
p1=1
p2=1
while(p1!=p2 or p1==1):
    p1=res[p1-1]
    p2=res[res[p2-1]-1]
if p1!=p2:
    print('wu')
else:
    idx=0
    while(p1!=p2 or idx==0):
        p1 = res[p1 - 1]
        p2 = res[res[p2 - 1] - 1]
        idx=idx+1
    print(idx)












# for i in a:

