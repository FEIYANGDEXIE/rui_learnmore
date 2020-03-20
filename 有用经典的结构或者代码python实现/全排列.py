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
    def bt(n,assign):
        # print(n,assign)
        if n==num:
            res.append(assign[:])
        elif n<num:

            for i in s:
                l_a = assign.copy()
                if len(assign)!=0:
                    if i>assign[-1]:
                        l_a.append(i)
                        bt(n+1,l_a)
                else:
                    l_a.append(i)
                    bt(n+1,l_a)




    bt(0,[])
    print(res)

    #组合




p([1,2,3,4,5],5)
c([1,2,3,4,5],2)