#1.Floyd算法是求任意两点之间的距离，是多源最短路，而Dijkstra(迪杰斯特拉)算法是求一个顶点到
# 其他所有顶点的最短路径，是单源最短路。
# 2.Floyd算法属于动态规划，我们在写核心代码时候就是相当于推dp状态方程，Dijkstra(迪杰斯特拉)算法属于贪心算法。
# 3.Dijkstra(迪杰斯特拉)算法时间复杂度一般是o(n^2),Floyd算法时间复杂度是o(n^3),Dijkstra(迪杰斯特拉)
# 算法比Floyd算法块。4.Floyd算法可以算带负权的，而Dijkstra(迪杰斯特拉)算法是不可以算带负权的。
# 并且Floyd算法不能算负权回路。

import copy
G2 = {1:{1:0,2:20},

     2:{2:0,3:30,4:25},

     3:{3:0,5:28},

     4:{4:0,5:32,6:95},

     5:{5:0,6:67},

     6:{6:0}}
def transfer(G):
    #从邻接表变成邻接矩阵
    num=len(G.keys())
    ans=[[999 for i in range(num)] for i in range(num)]
    for key in G:
        for key2,value2 in G[key].items():
            ans[key-1][key2-1]=value2
    print(ans)
    return  ans
def floyd(G):
    num=len(G)
    ans=copy.deepcopy(G)
    for k in range(num):
        #k代表动态规划递加
        for i in range(num):
            for j in range(num):

                if ans[i][j]>ans[i][k]+ans[k][j]:
                    ans[i][j] = ans[i][k] + ans[k][j]
    print(ans)
    return ans

linjie=transfer(G2)
floyd(linjie)



