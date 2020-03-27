n=5
m=4
data=[[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]


if m<=2 or n<=2:
    print(0)
else:
    ans = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        lab = 0
        lab1=0
        for j in range(m):
            if j != 0 and j !=m-1:
                ans[i][j] = lab
            lab = max(lab, data[i][j])
    for i in range(n):
        lab = 0
        for j in range(m):
            if j != 0 and j !=m-1:
                ans[i][-1-j] = min(lab,ans[i][-1-j])
            lab = max(lab, data[i][-1-j])
    for j in range(m):
        lab = 0
        for i in range(n):
            if i != 0 and i !=n-1:
                ans[i][j] = min(lab,ans[i][j])
            lab = max(lab, data[i][j])
    for j in range(m):
        lab = 0
        for i in range(n):
            if i != 0 and i !=n-1:
                ans[-1-i][j] = min(lab,ans[-1-i][j])
            lab = max(lab, data[-1-i][j])
    res=0
    for i in range(n):
        if i!=0 and i!=n-1:
            for j in range(m):
                if j!=0 and j!=m-1:

                    if ans[i][j]>data[i][j]:
                        print(i, j,ans[i][j]-data[i][j])
                        res=res+ans[i][j]-data[i][j]
    print(ans)
    print(res)
