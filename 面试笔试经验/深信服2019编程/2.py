class node:
    def __init__(self, val):
        self.val = val
        self.val_int = int(''.join(list(map(str, val))))

    def __lt__(self, other):
        return self.val_int < other.val_int


def fun1(idx, s, p_n):
    if p_n == 0:
        res.append(node(s))
    else:
        if idx >= 0:
            for i in range(min(d[idx], p_n), -1, -1):
                local_s = s.copy()
                local_s[idx] = i
                fun1(idx - 1, local_s, p_n - i)


kn = input().strip().split()
k = int(kn[0])
n = int(kn[1])
d = {}
for i in range(k):
    tmp = input().strip()
    tmp = int(tmp)
    d[i] = tmp
# print(d)

res = []
assign = [0 for i in range(len(d))]
fun1(len(d) - 1, assign, n)
res = list(sorted(res))
for i in range(len(res)):
    tmp = ''.join(list(map(str, res[i].val)))
    print(tmp)


