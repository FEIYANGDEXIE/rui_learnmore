import copy
def fun1(num, b):
    global ans
    if num == 2 * n - 1:
        l = 0
        for i in b:
            for j in i:
                if j == 2:
                    l = l + 1

        ans = max(ans, l)
    else:
        if num % 2 == 0:
            lab = 2
            f = 1
        else:
            lab = 1
            f = 2
        location = []
        for i in range(len(b)):
            for j in range(len(b[0])):
                if b[i][j] == f:
                    s = [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1], [i - 1, j - 1], [i - 1, j + 1], [i + 1, j - 1],
                         [i + 1, j + 1]]
                    for idx in s:
                        try:
                            if b[idx[0]][idx[1]] == 0:
                                location.append([idx[0], idx[1]])
                        except:
                            pass
        # location变化
        # print(location)
        for idx in location:
            local_b = copy.deepcopy(b)
            local_b[idx[0]][idx[1]] = lab
            i = idx[0]
            j = idx[1]
            s2 = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, 1], [-1, -1], [1, -1], [1, 1]]
            fz = 0
            for i2 in s2:
                idx2 = 0
                res = 0
                while (True):
                    i = i + i2[0]
                    j = j + i2[1]
                    idx2 = idx2 + 1
                    if i >= 0 and i < len(local_b) and j >= 0 and j < len(local_b[0]):
                        if idx2 == 1:

                            if local_b[i][j] != f:
                                res = 1
                                break
                            else:
                                res = 2
                        else:
                            if local_b[i][j] == lab:

                                res = 3
                                break
                            elif local_b[i][j] == 0:
                                res = 4
                                break
                    else:
                        res = -1
                        break
                if res == 3:
                    for idx3 in range(1, idx2):
                        local_b[idx[0] + idx3 * i2[0]][idx[1] + idx3 * i2[1]] = lab
                        fz = fz + 1
            if fz > 0:
                # print(num,fz)
                fun1(num + 1, local_b)

        # 找出所有可以落子的位置，迭代


n = input().strip()
n = int(n)
board = []
for i in range(8):
    tmp = input().strip().split()
    tmp = list(map(int, tmp))
    board.append(tmp[:])
# print(board)
ans = 0
fun1(0, board)
print(ans)
