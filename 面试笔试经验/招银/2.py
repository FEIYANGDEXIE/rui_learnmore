class node:
    def __init__(self, v, l=None, right=None):
        self.v = v
        self.l = l
        self.right = right


def preorder(r):
    if r:
        print(r.v)
        ans1.append(r.v)
    if r.l:
        preorder(r.l)
    if r.right:
        preorder(r.right)


def morder(r):
    pass


def lorder(r):
    pass


nr = input().strip().split()
n = int(nr[0])
root = int(nr[1])
# print(n,root)
d = {}

for i in range(n):
    tmp = input().strip().split()
    tmp = list(map(int, tmp))
    new = node(tmp[0])
    d[tmp[0]] = [new, tmp[1], tmp[2]]

for i in d:
    # print(d[i][0].v,d[i][1],d[i][2])
    if d[i][1] != 0:
        d[i][0].l = d[d[i][1]][0]
    if d[i][2] != 0:
        d[i][0].right = d[d[i][2]][0]
ans1 = []
preorder(d[root][0])
# print(ans1)