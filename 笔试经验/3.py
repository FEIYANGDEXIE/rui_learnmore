
def fun1(num):
    num=list(map(int,num))
    tag=''
    ans=0
    ans1=[]
    for idx, item in enumerate(range(num[1])):

        if idx<num[0]-1:
            tag = tag + str(idx + 1)
        elif idx==num[0]-1:
            tag = tag + str(idx + 1)
            lab=list(tag)
            lab=list(map(int,lab))
            total=sum(lab)
            remainder=total%3
            if remainder==0:
                ans=ans+1
            # print(lab,total)
        else:
            lab=list(str(idx+1))
            lab = list(map(int, lab))
            addp=sum(lab)
            total=total+addp
            remainder = total % 3
            if remainder == 0:
                ans = ans + 1
    return ans

a=['2', '500000']
bb=fun1(a)
print(bb)
