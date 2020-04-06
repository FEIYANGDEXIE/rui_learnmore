class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here

        if index == 1:
            return 1

        else:
            idx = 1
            i = 1
            lab = [2, 3, 5]
            while (idx < index):
                i = i + 1
                target = i
                d = 2
                while (target != 1 and d >= 0):
                    if target % lab[d] == 0:
                        target = target // lab[d]
                    else:
                        d = d - 1
                if target == 1:
                    idx = idx + 1
            print(i)
            return i
a=Solution()
a.GetUglyNumber_Solution(500)
