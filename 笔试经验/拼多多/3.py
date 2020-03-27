n=5
m=5
data=[[1,3,1,2,1],[2,1,3,1,1],[1,4,2,6,1],[1,3,1,3,1],[1,1,5,1,1]]
#参见leetcode文件下的407，上面有一种漏水解法 下面的从一维扩展的题有错误

ans = [[0 for j in range(m)] for i in range(n)]
if m<=2 or n<=2:
    print(0)
else:

    for i in range(n):
        lab=0
        for j in range(m):
            lab=max(lab,data[i][j])
            ans[i][j]=lab
    for i in range(n):
        lab=0
        for j in range(m-1,-1,-1):
            # print(j)
            lab=max(lab,data[i][j])
            ans[i][j]=min(lab,ans[i][j])
    for j in range(m):
        lab=0
        for i in range(n):
            lab = max(lab, data[i][j])
            ans[i][j] = min(lab, ans[i][j])
    for j in range(m):
        lab=0
        for i in range(n-1,-1,-1):
            lab = max(lab, data[i][j])
            ans[i][j] = min(lab, ans[i][j])
    res=0
    for i in range(n):
        for j in range(m):
            if ans[i][j]>data[i][j]:
                res=res+ans[i][j]-data[i][j]
    print(res)
