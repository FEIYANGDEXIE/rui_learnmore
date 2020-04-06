def fun1():
    print(lab)

    pass

def fun2():
    global a,b
    print(a,b)
    pass
lab=[0,0,0]
fun1()
a=0
b=1
fun2()