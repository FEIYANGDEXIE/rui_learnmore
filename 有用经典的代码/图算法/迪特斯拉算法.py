import heapq
#图是有向图还是无向图、是否有负权边，是否有重边，顶点到自身的可达性
G = {'a': {'a':0,'b': 6, 'd': 4, 'f': 1},

     'b': {'b':0,'c': 7,'d':7},

     'c': {'c': 0, 'd': 2,'e':4},

     'd': {'b':3,'c':5,'d': 0,'e':1,'f':7},

     'e': {'a': 2, 'd': 3,'e':0},

     'f': {'b':3,'c': 4,'e':4,'f':0}
}

G2 = {1:{1:0,2:1,3:12},

     2:{2:0,3:9,4:3},

     3:{3:0,5:5},

     4:{3:4,4:0,5:13,6:15},

     5:{5:0,6:4},

     6:{6:0}}


G3 = {1: {1: 0, 2: 1, 3: 12},

     2: {2: 0, 3: 9, 4: 3},

     3: {3: 0, 5: 5},

     4: {3: 4, 4: 0, 5: 13, 6: 15},

     5: {5: 0, 6: 4},

     6:{6: 0}}
class des:
    def __init__(self,destin,distance):
        self.destin=destin
        self.distance=distance
    def __lt__(self, other):
        return self.distance < other.distance


def Dij2(G,v0):

    minheap=[]
    # for i in G:
    #     heapq.heappush(minheap,des(i,999))
    keynum=len(G)
    for key,value in G[v0].items():
        heapq.heappush(minheap, des(key,value))
    # print(keynum)
    ans={}
    flag=0
    explored=[0 for i in range(keynum+1)]
    while(flag<keynum and len(minheap)>0):
        #最小堆需要支持任意remov
        res=heapq.heappop(minheap)
        if explored[res.destin]==0:
            explored[res.destin]=1
            flag=flag+1
            ans[res.destin]=res.distance
            for i in range(1,keynum+1):
                if explored[i] == 0:
                    try:
                        heapq.heappush(minheap,des(i,res.distance+G[res.destin][i]))
                    except:
                        pass

    # print(ll)
    return ans

def Dij(G,v0):
    keynum=0
    des={}
    # minheap=[]
    for i in G:

        des[i]=999
        keynum = keynum + 1
    keynum=len(G)
    for key,value in G[v0].items():
        des[key]=value
    print(keynum)
    ans={}
    flag=0

    while(flag<keynum):
        #最小堆需要支持任意remov
        ll=sorted(des.items(), key=lambda x: x[1])#必须是items 才能取到两个
        ele=ll[0][0]
        distance=ll[0][1]  #取得字典第一位的元素
        # print(ele,distance)
        ans[ele]=distance
        del des[ele]  #删除字典元素
        # print(des)
        for key,value in des.items():
            try:
                if value>distance+G[ele][key]:
                    des[key]=distance+G[ele][key]
                    # print (key)
            except:
                pass
        # print(des)
        flag=flag+1

    # print(ll)
    return ans

# 图为邻接表形式

# Dijkstra算法——通过边实现松弛

# 指定一个点到其他各顶点的路径——单源最短路径

# 初始化图参数


def Dijkstra(G, v0, INF=999):
    """ 使用 Dijkstra 算法计算指定点 v0 到图 G 中任意点的最短路径的距离

        INF 为设定的无限远距离值

        此方法不能解决负权值边的图
    """
    book = set()
    minv = v0  # 源顶点到其余各顶点的初始路程

    dis = dict((k, INF) for k in G.keys())

    dis[v0] = 0

    while len(book) < len(G):

        book.add(minv)  # 确定当期顶点的距离

        for w in G[minv]:  # 以当前点的中心向外扩散

            if dis[minv] + G[minv][w] < dis[w]:  # 如果从当前点扩展到某一点的距离小与已知最短距离

                dis[w] = dis[minv] + G[minv][w]  # 对已知距离进行更新

        new = INF  # 从剩下的未确定点中选择最小距离点作为新的扩散点

        for v in dis.keys():

            if v in book: continue

            if dis[v] < new:
                new = dis[v]

                minv = v

    return dis
print(Dij(G3,2))
# dis = Dijkstra(G3, v0=2)
# print(dis)
print(Dij2(G3,2))