#最短路径

# Bellman-Ford。算法 带负权的图
#
# 图为邻接表形式
# Dijkstra算法——通过边实现松弛
# 指定一个点到其他各顶点的路径——单源最短路径
# 初始化图参数
def bellford(G,v0):
    #没有负环， 遍历n-1次，遍历每个边
    ans={}
    des={}
    keynum=0
    for i in G:
        des[i]=999
        keynum=keynum+1
    des[v0]=0
    print(des)
    for i in range(keynum-1):
        #遍历所有边
        for key1 in G:
            for key2,value in G[key1].items():
                if des[key2]>des[key1]+value:
                    des[key2] = des[key1] + value
    print(des)

    return  ans

G3 = {1: {1: 0, 2: 1, 3: 12},

     2: {2: 0, 3: 9, 4: 3},

     3: {3: 0, 5: 5},

     4: {3: 4, 4: 0, 5: 13, 6: 15},

     5: {5: 0, 6: 4},

     6:{6: 0}}

bellford(G3,1)
