#最小优先队列 小顶堆实现
#最大优先队列 大顶堆实现
#双端优先队列，一个最小优先队列，一个最大优先队。Leaf Correspondence，Total Correspondence。1 buffer
#remove min,max 任意remove
#insert
#shift up,down

import heapq
li = [5, 7, 9, 1, 3]
heapq.heapify(li)
print ("The created heap is : ",end="")
print (list(li))
heapq.heappush(li,4)
print ("The modified heap after push is : ",end="")
print (list(li))

#heapq.push() heapq.pop() heap[0]