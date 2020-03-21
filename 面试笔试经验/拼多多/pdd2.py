m=80
data=[1,2,5]

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
