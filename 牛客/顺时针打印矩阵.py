class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        # print(matrix)
        labm=[[0 for j in range(len(matrix[0]))]for i in range(len(matrix))]
        i=0
        j=0
        lab=0
        d=[[0,1],[1,0],[0,-1],[-1,0]]
        ans=[]
        if len(matrix)==1 and len(matrix[0])==1:
            return [matrix[0][0]]
        while(labm[i][j]==0):
            # print(i,j)
            labm[i][j]=1
            ans.append(matrix[i][j])
            lab2=0
            p_lab=lab
            while(lab2==0 and lab-p_lab<4):
                # print(lab,p_lab,lab2,i,j)
                if d[lab%4][0]+i>=0 and d[lab%4][0]+i<len(matrix) and d[lab%4][1]+j<len(matrix[0]) and d[lab%4][1]+j>=0:


                    if labm[d[lab%4][0]+i][d[lab%4][1]+j]==0:
                        lab2=1
                        i = d[lab % 4][0] + i
                        j = d[lab % 4][1] + j

                    else:
                        lab=lab+1
                else:
                    lab=(lab+1)
        # print(ans)
        return ans
a=Solution()
mm=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
a.printMatrix(mm)