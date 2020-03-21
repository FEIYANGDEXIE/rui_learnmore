# import heapq
import copy

class Solution:
    def trapRainWater(self, heightMap) -> int:
        n = len(heightMap)
        m = len(heightMap[0])
        data = heightMap
        # for i in data:
        #     print(i)
        me=0
        for i in data:
            for j in i:

                me=max(me,j)

        # print(me)
        ans=copy.deepcopy(data)
        for i in range(n):
            if i!=0 and i!=n-1:
                for j in range(m):
                    if j!=0 and j!=m-1:
                        # print(i,j)
                        if ans[i][j]<me:
                            ans[i][j]=me
        # for i in ans:
        #     print(i)
        # print(ans)
        lab=1
        while(lab==1):
            lab=0

            for i in range(n):
                if i!=0 and i!=n-1:
                    for j in range(m):
                        if j!=0 and j!=m-1:
                            tmp=min(ans[i-1][j],ans[i+1][j],ans[i][j+1],ans[i][j-1])
                            if ans[i][j]>data[i][j] and ans[i][j]>tmp:
                                lab=1
                                if data[i][j]<tmp:
                                    ans[i][j]=tmp
                                else:
                                    ans[i][j]=data[i][j]
                                # print(i,j,tmp)
        res=0
        for i in range(n):
            if i != 0 and i != n - 1:
                for j in range(m):
                    if j != 0 and j != m - 1:
                        if ans[i][j]>data[i][j]:
                            res=res+ans[i][j]-data[i][j]


        # print(data)
        # for i in ans:
        #     print(i)
        # print(ans)
        # print(res)
        return res









data2=[[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
data3=[[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]
so=Solution()
so.trapRainWater(data2)




