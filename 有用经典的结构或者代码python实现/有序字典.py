from collections import OrderedDict
import copy
st1='abbbcafdh'
st2='abc'
def fun2(s1,s2):
    i=0
    j=0
    st1=list(s1)
    st2=list(s2)
    while(i<len(st1) and j<len(st2)):
        pass
    pass
def fun1(s1,s2):
    s2 = list(s2)
    d = OrderedDict()
    for i in range(len(s1)):
        # print(i,d)
        if len(d) == len(s2):
            print(d)
            c = copy.deepcopy(d)
            f = c.popitem()

            l = c.popitem(last=False)
            print(f[1] - l[1] + 1)
            try:
                m=min(m,f[1] - l[1] + 1)
            except:
                m=f[1] - l[1] + 1
        if s1[i] in s2:
            if s1[i] in d:
                d[s1[i]] = i
                d.move_to_end(s1[i])
            else:
                d[s1[i]] = i
    return m

ans=fun1(st1,st2)

print(ans)





