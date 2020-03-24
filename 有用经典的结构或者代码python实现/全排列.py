from itertools import permutations,combinations

a=list(permutations([1,2,3,4,5],5))
print(a)
b=list(combinations([1,2,3,4,5],2))
print(b)
def p(s,num):
    #排列
    res=[]
    def bt(n,assign):
        if n==num:
            res.append(assign[:])
        elif n<num:
            for i in s:
                if i not in assign:
                    l_a=assign.copy()
                    l_a.append(i)
                    bt(n+1,l_a)
    bt(0,[])
    print(res)

def c(s,num):
    res=[]
    def bt(n,n2,assign):
        # print(n,assign)
        if n==num:
            res.append(assign[:])
        elif n<num:
            for i in range(n2,len(s)):
                l_a = assign.copy()

                l_a.append(s[i])
                bt(n+1,i+1,l_a)
    bt(0,0,[])
    print(res)

    #组合




p([1,2,3,4,5],5)
c([1,2,3,4,5],2)