import math
def fun1(a):
    num1=float(a[0]-a[2])
    num2=float(a[1]-a[3])
    d=math.sqrt(num1*num1+num2*num2)
    # print(d)
    # format(float(d)/float(a[4]),'.3f')
    f=d/float(a[4])
    return f
a=[1,1,2,2,1]
fun1(a)