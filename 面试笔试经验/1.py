#数据分类处理
def fun1(a_i,a_j):
    a_j=list(map(int,a_j))
    a_j=a_j[1:]
    a_j=sorted(set(a_j))
    a_j=[str(x) for x in  a_j]

    ans=[]
    for item in a_j:
        c1=list(item)

        mid=[]
        for idx,tag in enumerate(a_i[1:]):
            c2=list(tag)
            for idx2,i in enumerate(tag):
                if item==''.join(tag[idx2:idx2+len(item)]):
                    mid.append(idx)
                    mid.append(tag)
                    break

        if len(mid)>0:

            ans.append(item)
            ans.append(int(len(mid)/2))
            ans=ans+mid
    ans2=[str(len(ans))]+ans
    ans2=[str(x) for x in ans2]

    return ' '.join(ans2)
i=['59', '10276', '7322', '9661', '7005', '11766', '1857', '2942', '8620', '9293', '5321', '2309', '3819', '9189', '3744', '1274', '3074', '1327', '8893', '4147', '4190', '3223', '1537', '407', '7508', '2347', '2060', '3336', '6547', '5926', '1067', '6194', '11531', '2372', '4795', '9153', '2441', '9959', '5413', '1089', '3048', '11817', '7808', '434', '11637', '3849', '10343', '162', '1578', '11395', '3913', '2380', '9214', '11422', '6835', '5970', '1128', '8650', '3309', '6598']
j=['25', '31', '38', '2', '95', '9', '97', '14', '105', '13', '86', '113', '122', '98', '17', '78', '71', '37', '32', '36', '7', '46', '92', '79', '68', '710']
print(fun1(i,j))
