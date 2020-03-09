import numpy as np
import heapq
a=[]

class node:
    def __init__(self,val1,val2):
        self.val1=val1
        self.val2=val2
    #比较功能
    def __lt__(self, other):
        return self.val2<other.val2

heapq.heappush(a,node('1',2))
heapq.heappush(a,node('2',3))
heapq.heappush(a,node('3',4))
# heapq.heappush(a,5)
# heapq.heappush(a,6)
# heapq.heappush(a,8)
# heapq.heappush(a,2)

print(a)
c=heapq.heappop(a)
print(c.val2)
# b=np.zeros([2,3])
# print(a,b)

