m=80
data=[1,2,5]
#题目印象中是有n个盒子，第i个盒子有i个球
#每次选择一个数字x，则所有盒子里大于等于x的球减少x个
#输出最少的次数将所有盒子球变没有
#比如2是1，2 ，3 减1变成0 1 2 再减1变成 0 0 1 再减去1变没有，所以是3次



for i in data:
    tmp=bin(i)
    print(len(tmp)-2)

# d = {}
# d[1] = 1
# for i in range(1, m+1):
#     if i > 1:
#         d[i] = d[i // 2] + 1
# for i in data:
#     print(d[i])
