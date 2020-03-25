def fun1(arg1):
    l=list(arg1)

    total=0
    for item in l:
        if item=='x':
            continue
        else:
            try:
                this_num=int(item)
                total=total*16+this_num
            except:
                this_num=ord(item)-55
                total = total * 16 + this_num

    return total

a=fun1('0xA')
print(a)