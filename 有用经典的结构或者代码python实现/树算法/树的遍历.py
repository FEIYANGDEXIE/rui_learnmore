#红黑树
#线段树
#斐波那契树
#极左树
#B树
'''
深度优先遍历：对每一个可能的分支路径深入到不能再深入为止，而且每个结点只能访问一次。要特别注意的是，二叉树的深度优先遍历比较特殊，可以细分为先序遍历、中序遍历、后序遍历。具体说明如下：
先序遍历：对任一子树，先访问根，然后遍历其左子树，最后遍历其右子树。
中序遍历：对任一子树，先遍历其左子树，然后访问根，最后遍历其右子树。
后序遍历：对任一子树，先遍历其左子树，然后遍历其右子树，最后访问根。
广度优先遍历：又叫层次遍历，从上往下对每一层依次访问，在每一层中，从左往右（也可以从右往左）访问结点，访问完一层就进入下一层，直到没有结点可以访问为止。
'''
#定义二叉树
class Node():
    def __init__(self,item,lchild=None,rchild=None):
        self.item=item
        self.lchild=lchild
        self.rchild=rchild
class Tree():
    def __init__(self,root=None):
        self.root=root
    def add(self,data):
        node=Node(data)
        if self.root==None:
            self.root=node
        else:
            quene=[]
            quene.append(self.root)
            while quene:
                cur=quene.pop(0)
                if cur.lchild==None:
                    cur.lchild=node
                    return
                elif cur.rchild==None:
                    cur.rchild=node
                    return
                else:
                    quene.append(cur.lchild)
                    quene.append(cur.rchild)
    def bfs(self):
        if self.root==None:
            return
        else:
            quene=[]
            quene.append(self.root)
            while quene:
                cur=quene.pop(0)
                print(cur.item)
                if cur.lchild is not None:
                    quene.append(cur.lchild)
                if cur.rchild is not None:
                    quene.append(cur.rchild)
    def dfspreorder(self,node):
        if node==None:
            return
        else:
            print(node.item)
            self.dfspreorder(node.lchild)
            self.dfspreorder(node.rchild)



a=Tree()
a.add(1)
a.add(2)
a.add(3)
a.add(4)
a.add(5)
a.add(6)
# a.bfs()
a.dfspreorder(a.root)

