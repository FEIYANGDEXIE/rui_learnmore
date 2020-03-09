
#股票序列，如何计算买入卖出最大，找到差值最大的两个数
shuru=[4,1,5,8,6,9,10,4]
def get2loc(a):
    minf=a[0]
    diff=0
    for i in a:
        if i>=minf:
            diff=max(diff,i-minf)


        else:
            minf=i
    print(minf,diff)

    return
get2loc(shuru)
