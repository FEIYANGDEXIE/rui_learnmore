def fun1(a,b):

    for item in b:
        ans=item[:-1]+item[-1].upper()
        print(ans)
    return ans



a=2
b=['abc','bcA']
c=fun1(a,b)

