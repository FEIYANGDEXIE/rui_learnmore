def fun1(a0,b0,i):
    # print(a0,b0,i)
    # print(len(data))
    if lab[0]==0:
        if a0==b0:
            # print(i)
            lab[0]=i
        else:
            for data in cal:
                fun1(a0+data,b0,i+1)
    else:
        if i<lab[0]:
            if a0==b0:
                # print(i)

                lab[0] = i
            else:
                for data in cal:
                    fun1(a0 + data, b0, i + 1)
cal=[12,-12,7,-7,5,-5]
a=-5
b=19
# data=[-5,0,7,9]
lab=[0]
fun1(a,b,0)
print(lab[0])