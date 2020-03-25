import sys
def fun1(a,b,nm):
    a=a.replace(' ','')
    a=list(a)
    a=list(map(int,a))
    jilu=a
    mydic={0:0,1:1,2:0}
    for item in b:
        start=int(item[0])-1
        finish=int(item[1])-1
        if start>finish:
            tmp=start
            start=finish
            finish=tmp
        for i in range(start,finish+1):
            jilu[i]=mydic[jilu[i]+1]
            # jilu[i]=(jilu[i]+1)
    # for idx,item in enumerate(jilu):

    #     jilu[idx]=jilu[idx]%2
    jilu=list(map(str,jilu))
    print(''.join(jilu))
    return a
a='00000'
b=[[1,3],[5,3]]
c=fun1(a,b,'5 2')
