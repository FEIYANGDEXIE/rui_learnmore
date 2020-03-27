#选择枢纽左右排序，交换法，挖坑法
#quicksort
a=[2,3,1,7,5,9,10,0]

def quicksort(s):
    # print(s)
    if len(s)<=1:
        return s
    elif len(s)==2:
        return [min(s),max(s)]
    else:
        t=s[0]
        q1=[]
        q2=[]
        for i in s[1:]:
            if i>t:
                q2.append(i)
            else:
                q1.append(i)
        q1=quicksort(q1)
        q1.append(t)
        q2=quicksort(q2)
        q=q1+q2
        return q
print(a)
t=quicksort(a)
print(t)
def mergesort(s):

    if len(s)==1:
        return s
    else:
        ans = []
        m=len(s)//2
        l=s[:m]
        r=s[m:]
        l=mergesort(l)
        r=mergesort(r)
        i=0
        j=0
        while(i<len(l) or j<len(r)):
            if i==len(l):
                ans.append(r[j])
                j=j+1
            elif j==len(r):
                ans.append(l[i])
                i=i+1
            else:
                if l[i]<r[j]:
                    ans.append(l[i])
                    i=i+1
                else:
                    ans.append(r[j])
                    j=j+1
        return ans
print(mergesort(a))
