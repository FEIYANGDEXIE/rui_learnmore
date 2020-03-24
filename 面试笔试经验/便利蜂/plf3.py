a='330,450,630,690,750,780,990,1050'
#
a=a.split(',')
a=list(map(int,a))
ans=[]
for i in range(0,len(a),2):
    a[i]=a[i]-30
    ans.append([a[i],0])
    a[i+1]=a[i+1]+30+60
    ans.append([a[i+1],1])
ans=list(sorted(ans))
res=[]
lab=0
for i in ans:
    if i[1]==0 and lab==0:
        lab=lab+1
        res.append(i[0])
    elif i[1]==0 and lab!=0:
        lab=lab+1
    elif i[1]==1 and lab-1==0:
        lab=lab-1
        res.append(i[0]-60)
    else:
        lab=lab-1

res=list(map(str,res))
print(','.join(res))















