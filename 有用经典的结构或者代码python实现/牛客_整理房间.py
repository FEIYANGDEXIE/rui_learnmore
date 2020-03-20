import copy
def fun2(m2):
    res=0
    ans = []
    ans.append((m2[0][0] - m2[1][0]) ** 2 + (m2[0][1] - m2[1][1]) ** 2)
    ans.append((m2[0][0] - m2[2][0]) ** 2 + (m2[0][1] - m2[2][1]) ** 2)
    ans.append((m2[0][0] - m2[3][0]) ** 2 + (m2[0][1] - m2[3][1]) ** 2)
    ans.append((m2[1][0] - m2[2][0]) ** 2 + (m2[1][1] - m2[2][1]) ** 2)
    ans.append((m2[1][0] - m2[3][0]) ** 2 + (m2[1][1] - m2[3][1]) ** 2)
    ans.append((m2[2][0] - m2[3][0]) ** 2 + (m2[2][1] - m2[3][1]) ** 2)
    #print(ans)
    if len(set(ans))==2 and 0 not in ans:
        a=0
        b=0
        s_a=list(set(ans))
        for i in ans:
            if i==s_a[0]:
                a=a+1
            if i==s_a[1]:
                b=b+1
        if a==4 and b==2:
            res=1
        if a==2 and b==4:
            res=1
    return res
def fun1(matrix, r):
    #print(r)
    distance = fun2(matrix)

    if distance== 1:
        #print('s',r)
        try:
            lab[0] = min(lab[0],sum(r[:4]))
        except:
            lab[0]=sum(r[:4])
        #print(lab[0])
    else:
        if r[4] <4:
            if lab[0]=='x':
                l_r = r.copy()
                l_matrix = copy.deepcopy(matrix)
                i=l_r[4]
                l_r[4]=l_r[4]+1
                fun1(l_matrix, l_r)
                x = matrix[i][0]
                y = matrix[i][1]
                a = matrix[i][2]
                b = matrix[i][3]
                l_matrix[i][0] = b - y + a
                l_matrix[i][1] = x - a + b
                l_r[i] = 1
                fun1(l_matrix, l_r)
                l_matrix[i][0] = 2*a-x
                l_matrix[i][1] = 2*b-y
                l_r[i] = 2
                fun1(l_matrix, l_r)
                l_matrix[i][0] = a+y-b
                l_matrix[i][1] = b+a-x
                l_r[i] = 3
                fun1(l_matrix, l_r)
            else:
                if lab[0]<sum(r[:4]):
                    l_r = r.copy()
                    l_matrix = copy.deepcopy(matrix)
                    i = l_r[4]
                    l_r[4] = l_r[4] + 1
                    fun1(l_matrix, l_r)
                    x = matrix[i][0]
                    y = matrix[i][1]
                    a = matrix[i][2]
                    b = matrix[i][3]
                    l_matrix[i][0] = b - y + a
                    l_matrix[i][1] = x - a + b
                    l_r[i] = 1
                    fun1(l_matrix, l_r)
                    l_matrix[i][0] = 2 * a - x
                    l_matrix[i][1] = 2 * b - y
                    l_r[i] = 2
                    fun1(l_matrix, l_r)
                    l_matrix[i][0] = a + y - b
                    l_matrix[i][1] = b + a - x
                    l_r[i] = 3
                    fun1(l_matrix, l_r)

n = input().strip()
n = int(n)
for i in range(n):
    data = []
    lab = ['x']
    for j in range(4):
        tmp = input().strip().split()
        tmp = list(map(int, tmp))
        data.append(tmp[:])
    # print(data)
    rotate = [0 for i in range(5)]
    fun1(data, rotate)
    if lab[0]=='x':
        print(-1)
    else:
        print(lab[0])