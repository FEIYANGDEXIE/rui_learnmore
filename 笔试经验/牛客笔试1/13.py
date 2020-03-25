def fun1(a):
    k=a[0]
    x1=a[1]
    x2=a[2]
    x_num=x2-x1+1
    y1=a[3]
    y2=a[4]
    y_num=y2-y1+1
    all=y_num*x_num
    zheng=2**(k-1)
    x_zheng=zheng-x1+1
    y_zheng=zheng-y1+1
    if x_zheng>0:
        if y_zheng>0:
            bu1=x_zheng*y_zheng-1
    # print(bu1)
    print(str(format(float(all-bu1)/float(all),'.6f')))

    return a
def fun2(a):
    k = a[0]
    x1 = a[1]
    x2 = a[2]
    x_num = x2 - x1 + 1
    y1 = a[3]
    y2 = a[4]
    y_num = y2 - y1 + 1
    total=0
    all = y_num * x_num
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            if i+j>=-(2**k):
                if i+j<=(2**k-1):
                    total=total+1
    print(str(format(float(all-total) / float(all), '.6f')))
    return a




a=[2,1,3,1,3]
fun2(a)
