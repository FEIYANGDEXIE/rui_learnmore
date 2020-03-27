class node:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def __eq__(self,other):
        return self.c==other.c
    def __lt__(self, other):
        return self.c<self.c

s1=node(1,2,3)
s2=node(2,5,3)
print(s1==s2)
print(s2>s2)