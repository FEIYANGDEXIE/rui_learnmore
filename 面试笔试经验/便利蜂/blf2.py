a='[1,2],[2,3],[3,4],[4,5],[5,3]'
#
class node:
    def __init__(self,v):
        self.v=v
        self.next=None

a=a.split(',')
# print(a)
ans=[]
for i in a:
    tmp=''
    for j in i:
        if j.isdigit():
            tmp=tmp+j
    ans.append(int(tmp))
# print(ans)
d={}
for i in list(set(ans)):

    new=node(i)
    d[i]=new
# print(d)
for i in range(0,len(ans),2):
    if i==0:
        head=d[ans[i]]
    d[ans[i]].next=d[ans[i+1]]
p1=head
p2=head
lab=0
while(p1 and p2):

    p1=p1.next
    if p2.next!=None:
        p2=p2.next.next
    else:
        break
    if p1==p2:
        lab=1
        start=p1
        break
# print(lab)
if lab==0:
    print(0)
else:
    p1=start.next
    p2=start.next.next
    idx=1

    while(p1!=p2):
        p1=p1.next
        p2=p2.next.next
        idx=idx+1
    print(idx)







# for i in a:

