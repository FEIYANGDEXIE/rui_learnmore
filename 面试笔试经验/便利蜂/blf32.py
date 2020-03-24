a='330,450,630,690,750,780,990,1050'
#
def backtrack(num,assign):
    lab=0
    for i in range(num,len(assign),2):
        if i+2<len(assign):
            if assign[i+1]+60>=assign[i+2]:
                lab=1
                l_a=assign.copy()
                l_a[i+1]=l_a[i+3]
                del l_a[i+3]
                del l_a[i+2]
                backtrack(i,l_a)
    if lab==0:
        print(assign)

a=a.split(',')
a=list(map(int,a))
ans=[]
for i in range(0,len(a),2):
    a[i]=a[i]-30
    ans.append(a[i])
    a[i+1]=a[i+1]+30
    ans.append(a[i+1])

backtrack(0,ans)

















