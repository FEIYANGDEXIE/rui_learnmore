#kruskal算法
# prime算法
#遍历边，不断加点
import heapq


def prime(nodes,edge_list):
    num=len(nodes)
    nodes=list(nodes)
    ans=[[999 for i in range(num)]for j in range(num)]
    dict_edge={}
    idx=0
    for item in nodes:
        if item not in dict_edge:
            dict_edge[item]=idx
            idx=idx+1
    dict_reverse={v:k for k,v in dict_edge.items()}
    # print(dict_reverse)
    # print(dict_edge)
    for item in edge_list:
        ans[dict_edge[item[0]]][dict_edge[item[1]]]=item[2]
    tmp=[]
    ans2=[]
    tmp.append(dict_reverse[0])
    minheap=[]
    #tmp记录已经选过的点
    while(len(tmp)<num):
        re_edge=[]
        for item in edge_list:
            if item[0] in tmp and item[1] not in tmp:
                re_edge.append(item)
            elif item[1] in tmp and item[0] not in tmp:
                re_edge.append((item))
        re_edge=list(sorted(re_edge,key=lambda x:x[2]))
        if re_edge[0][0] in tmp:
            tmp.append(re_edge[0][1])
        else:
            tmp.append(re_edge[0][0])
        ans2.append(re_edge[0])
        # print(tmp)
    # while(len(ans2)<len(nodes)):
    #
    #
    #     tmp=[]
    #     for item in edge_list:
    #         if item[0]==
    print(ans2)
    return ans2


def krustral(node,edge_list):
    node=list(node)
    num=len(node)
    dict_node={}
    idx=0
    for item in node:
        if item not in dict_node:
            dict_node[item]=idx
            idx=idx+1
    #边排序
    edge_list=list(sorted(edge_list,key=lambda x:x[2]))
    # print(edge_list)
    ans=[]
    #从小到大选边，使用dict记录已选的边的点并更新
    for item in edge_list:
        v1=dict_node[item[0]]
        v2=dict_node[item[1]]
        if v1==v2:
            continue
        elif v1>v2:
            for key,value in dict_node.items():
                if value==v1:
                    dict_node[key]=v2
            dict_node[item[0]]=v2
            ans.append(item)
        else:

            for key,value in dict_node.items():
                if value==v2:
                    dict_node[key]=v1
            ans.append(item)

        # print(dict_node)
    print(ans)
    return ans
nodes = set(list('ABCDEFGHI'))

edges = [("A", "B", 4), ("A", "H", 8),

        ("B", "C", 8), ("B", "H", 11),

        ("C", "D", 7), ("C", "F", 4),

        ("C", "I", 2), ("D", "E", 9),

        ("D", "F", 14), ("E", "F", 10),

        ("F", "G", 2), ("G", "H", 1),

        ("G", "I", 6), ("H", "I", 7)]

class ee:
    def __init__(self,u,v,d):
        self.u=u
        self.v=v
        self.d=d

    def __lt__(self, other):
        return self.d<other.d

def prime2(nodes, edge_list):
    num = len(nodes)
    nodes=list(nodes)
    d={}
    for i in nodes:
        d[i]=0
    # print(d)
    d[nodes[0]]=1
    minheap=[]
    for i in edge_list:
        if d[i[0]]==0 and d[i[1]]==1:
            heapq.heappush(minheap,ee(i[0],i[1],i[2]))


        elif d[i[0]]==1 and d[i[1]]==0:
            heapq.heappush(minheap, ee(i[0], i[1], i[2]))
    flag=0
    ans=[]
    while(flag<len(nodes)-1):
        tmp=heapq.heappop(minheap)
        if d[tmp.u]==1 and d[tmp.v]==1:
            continue
        ans.append(tmp)
        flag=flag+1
        d[tmp.u]=1
        d[tmp.v]=1
        for i in edge_list:
            if d[i[0]] == 0 and d[i[1]] == 1:
                heapq.heappush(minheap, ee(i[0], i[1], i[2]))


            elif d[i[0]] == 1 and d[i[1]] == 0:
                heapq.heappush(minheap, ee(i[0], i[1], i[2]))

    for i in ans:

        print(i.u,i.v,i.d)




    # print(nodes)


# krustral(nodes,edges)
prime(nodes,edges)
prime2(nodes,edges)