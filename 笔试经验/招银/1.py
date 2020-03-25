# //使用回溯法解决，我确实对java不熟，这里裸写python了
def fun(num,st):
    global ans
    if num <= 1:
        for i in range(s2[num]):
            if int(st[:i + 1]) <= s[num]:
                print(num, st[:i + 1], ans)
                local_st = st[i + 1:]
                fun(num + 1, local_st)
    if num == 2:
        if int(st) <= s[num]:
            ans = ans + 1
n='245235'
# //这里假设n是字符串输入
s=[180,90,3000]
s2=[3,2,4]
ans=0
fun(0,n)
print(ans)