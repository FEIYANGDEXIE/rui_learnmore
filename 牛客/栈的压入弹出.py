class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        self.s2=[]
        lab=0
        ans=0
        for i in popV:

            # print(self.s2,pushV)
            if lab==0:
                tmp = pushV.pop()
                while(tmp!=i and lab==0 and pushV):
                    self.s2.append(tmp)
                    tmp=pushV.pop()
                if tmp==i:
                    lab=1
                else:
                    ans=1
                    break
            else:
                if len(pushV)>0:
                    if pushV[-1]==i:
                        pushV.pop()
                    else:

                        while(self.s2):
                            tmp=self.s2.pop(0)
                            if tmp==i:

                                break
                            else:
                                pushV.append(tmp)
                        if tmp!=i:
                            ans=1
                            break
                else:
                    while (self.s2):
                        tmp = self.s2.pop(0)
                        if tmp == i:

                            break
                        else:
                            pushV.append(tmp)
                    if tmp != i:
                        ans = 1
                        break
        # print(ans)
        if ans==0:
            return True
        else:
            return False







a=Solution()

a.IsPopOrder([1,2,3,4,5],[4,3,5,1,2])