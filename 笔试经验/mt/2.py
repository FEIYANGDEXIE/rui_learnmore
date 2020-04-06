n=4
m=21
data=[2,1,4,3]

#
t=m
li=[i+1 for i in range(len(data))]
li[len(data)-1]=0
res2=0
mi=min(data)
res=0
j=0
while(t>=mi):
    if t-data[j]>=0:
        t=t-data[j]
        res = res + 1

    j=li[j]

# print(res)
res2=max(res2,res)
print(res2)




