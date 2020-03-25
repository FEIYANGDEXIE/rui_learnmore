import math
n = input()
a = {}
prime = [2]
flag = 0
for i in range(n):
    holder = input()
    if holder == 1:
        print ('Impossible')
        flag = 1
        break
    a[holder] = 1

if flag == 0 and not a.get(2):
    print (1, 20)
else:
    index = 3
    while(flag == 0):
        for p in prime:
            if index % p == 0:
                break
            elif p*p>index:
                prime.append(index)
                if not a.get(index):
                    print (1, index)
                    flag = 1
                break
        if index % 3 == 1:
            if index % 5 == 1:
                index += 6
            else:
                index += 4
        else:
            index += 2
