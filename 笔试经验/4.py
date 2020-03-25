#牛客校招真题安置路灯。注意字符的大小写问题
def fun1(a, b):
    lukuang = list(b)
    idx2 = 0
    total = 0
    while (idx2 < a):
        if lukuang[idx2] == 'X':
            idx2 = idx2 + 1
            # print(idx2)
            continue
        elif lukuang[idx2] == '.':
            total = total + 1
            idx2 = idx2 + 3
    return total

fun1(11,'...XX....XX')