#当数据插入很多，数据读取都是遍历的时候，链表最为方便
class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

node1=Node(1)
node2=Node(2)
node3=Node(3)
node23=Node(5)

node1.next=node2
node2.next=node3
node23.next=node1
a=node23
while a.next!=None:

    a=a.next

    print(a.data)
    a.data = 5
a=node23
while a.next!=None:

    a=a.next
    a.value=5
    print(a.data)

#单链表反转
def reverselinklist(phead):
    if not phead or not phead.next:
        return phead
    last=None
    while phead:

        tmp=phead.next
        phead.next=last
        last=phead
        phead=tmp
    return last

#单链表快速排序
