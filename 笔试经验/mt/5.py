data=[1,3,5,8]
if len(data)%2==1:
    print(0)
else:
    if len(data)==0:
        print(0)
    else:

        ans=0
        for i in range(len(data)):
            ans=ans^data[i]
        print(ans)
        # print(1^3^5^8)
print(0^5)