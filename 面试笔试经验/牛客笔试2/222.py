import sys


def fun1(n, m):
    for i in range(2, n):
        while (n % i == 0 and m % i == 0):
            n = n // i
            m = m // i
    # print(n,m)

    return n, m


nm = sys.stdin.readline().strip()
nm = list(map(int, nm.split()))
if nm[0] < nm[1]:
    print('0/1')
elif nm[0] > nm[1]:
    if nm[0] * nm[1] > 0:
        print('1/0')
    else:
        print('-1/0')
else:
    a = sys.stdin.readline().strip()
    a = list(map(int, a.split()))
    b = sys.stdin.readline().strip()
    b = list(map(int, b.split()))
    x = a[0]
    y = b[0]
    if a[0] < 0:
        x = -1 * x
    if b[0] < 0:
        y = -1 * y

    if a[0] > 0 and b[0] > 0:
        print(str(a[0]) + '/' + str(b[0]))
    elif a[0] < 0 and b[0] < 0:
        print(str(x) + '/' + str(y))
    else:
        print('-' + str(x) + '/' + str(y))



def fun1(a):
    i=0
    ans=[]
    while(len(ans)<2 and i<10**5):
        pro=1
        for item in a:
            tmp = i % item
            pro=pro*tmp
        if pro !=0:
            ans.append(i)
            # print(i)
        # print(pro,i)
        i=i+1
    return ans