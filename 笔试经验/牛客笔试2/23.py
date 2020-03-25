def fun1(n,m):
    for i in range(2,n):
        while(n%i==0 and m%i==0):
            n=n//i
            m=m//i
    #print(n,m)

    return n,m

fun1(1,2)