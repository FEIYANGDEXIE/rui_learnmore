# -*- coding:utf-8 -*-
#        10
# .    6.     14
# . 4.   8. 12.  16
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        def bt(node):
            print(node.val)
            if node:
                if node.left:
                    tmp = bt(node.left)
                    p = tmp
                    while (p.right!=None):
                        print('aa',p.val)
                        p = p.right
                    print('s',p.val)
                    node.left = p
                    p.right = node
                else:
                    tmp = node
                if node.right:
                    tmp2 = bt(node.right)
                    node.right = tmp2
                    tmp2.left = node
            test=tmp
            print(tmp)
            while(test):
                print('aaa',test.val)
                test=test.right
            return tmp
        p = pRootOfTree

        return bt(p)

        # write code here
a=TreeNode(10)
a.left=TreeNode(6)
a.right=TreeNode(14)
a.left.left=TreeNode(4)
a.left.right=TreeNode(8)
a.right.left=TreeNode(12)
a.right.right=TreeNode(16)
aa=Solution()
ans=aa.Convert(a)
print(ans)
while(ans):
    print(ans.val)
    ans=ans.right
