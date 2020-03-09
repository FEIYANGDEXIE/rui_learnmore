a=[4,2,15,5]
'''
a 4 b 2,\ 15 5      
      5   2. 15
a 5 
a 15 1
b 2
有两个人，只能从两端拿数，判断获胜的条件是谁拿的数最大，判断先拿的选手能不能先获胜呢
'''

start=0
end=len(a)-1

s1=[]
s2=[]
flag=0
ans= []
ans2=[]
def fun1(i,j,tmp1,tmp2):

    if i==j:
        tmp1.append(a[i])
        ans2.append(tmp2[:])
        ans.append(tmp1[:])
        #list dict只传递空值
        print(tmp1,tmp2)
        tmp1.pop()
        return
    else:
        tmp1.append(a[j])
        j=j-1
        fun1(i,j,tmp2,tmp1)
        tmp1.pop()
        j=j+1
        tmp1.append(a[i])
        i = i + 1
        fun1(i, j,tmp2,tmp1)
        tmp1.pop()
        i = i - 1

fun1(start,end,s1,s2)
print(ans2)
print(ans)








