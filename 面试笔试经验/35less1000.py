s1=3
s2=5
def fun1(s):
    r=1000//s
    if 1000%s!=0:
        return s*(1+r)*r//2
    else:
        return s*(1+r-1)*(r-1)//2
def fun2(a,b):
    for i in range(1,a*b+1):
        if i%a==0 and i%b==0:
            break
    return i
# print(fun1(s1))
# print(fun1(s2))
s3=fun2(s1,s2)
ans=fun1(s1)+fun1(s2)-fun1(s3)
print(ans)




