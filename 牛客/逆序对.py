# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        def fun1(target):
            i = 0
            j = len(ans) - 1
            if j == -1:
                return 0
            while (j - i > 1):
                m = (i + j) // 2
                if ans[m] > target:
                    j = m
                else:
                    i = m
            if ans[i] > target:
                return i
            elif ans[j] < target:
                return j + 1
            else:
                return j

        ans = []
        s = 0
        for i in data:
            n = fun1(i)
            print(n,i)
            num = len(ans) - n
            ans.insert(n, i)
            if num>0:
                s = s + num

        return s


a=Solution()
a.InversePairs([1,2,3,4,5,6,7,0])