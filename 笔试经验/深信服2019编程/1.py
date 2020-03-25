def fun1(i, j):
    if j == len(sub):
        res.append(i)
    elif j < len(sub) and i < len(s):

        if sub[j] != '?':
            if sub[j] == s[i]:
                fun1(i + 1, j + 1)
        else:
            for idx in range(1, 4):
                fun1(i + idx, j + 1)


s = input().strip()
s = list(s)
sub = input().strip()
sub = list(sub)
# print(s,sub)
res = []
fun1(0, 0)
if len(res) == 0:
    print(-1)
else:
    print(min(res))
