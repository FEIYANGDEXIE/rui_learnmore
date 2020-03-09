#背包问题，
#背包九讲


def get_count(n):
    #十个格子，每步走一步或两步，共有多少种走法。
    if n == 1:return 1
    elif n == 2 :return 2
    else:
        l = [1,2]
        for i in range(3,n):
            l[0],l[1] = l[1],l[0]+l[1]
        return l[0]+l[1]
# print(get_count(10))

import os

def count_min():
    # 如果我们有面值为 1 元、3 元和 5 元的硬币若干枚，如何用最少的硬币凑够 11 元？
    Min = [x for x in range(12)];
    VN = [1, 3, 5];
    for i in range(1, 12, 1):
        for j in range(3):
            if VN[j] <= i and Min[i - VN[j]] + 1 < Min[i]:
                Min[i] = Min[i - VN[j]] + 1;
    print(Min[1::1]);
def count_min_cr():
    zt=[x for x in range(12)]
    vn=[0,1,3,5]
    ans=[[0 for x in range(12)] for x in range(len(vn)+1)]
    for i in range(1,len(vn)+1):
        for j in range(1,12):
            if (j>vn[i]):
                print(1)


    print(ans)

# count_min_cr()






